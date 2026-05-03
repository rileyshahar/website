# Mirrors the (inst, code/title) merging in scripts/build_cv.py so the site can
# show one row per course with its terms collapsed into ranges.

module TeachingMerge
  TERM_ORDER = { "Spring" => 0, "Summer" => 1, "Fall" => 2 }.freeze
  SEMESTERS_PER_YEAR = 3
  # Spring -> Fall has a gap of 2 (Summer between); collapse into a single range.
  MAX_CONSECUTIVE_GAP = 2

  module_function

  def semester_index(year, term)
    year.to_i * SEMESTERS_PER_YEAR + TERM_ORDER.fetch(term, 0)
  end

  def sort_key(entry)
    [
      -entry["year"].to_i,
      -(TERM_ORDER[entry["term"]] || 5),
      (entry["week"] || 0).to_i,
    ]
  end

  def format_term_ranges(term_years)
    return "" if term_years.empty?
    indexed = term_years.uniq.map { |y, t| [semester_index(y, t), t, y] }.sort
    runs = []
    start = prev = indexed.first
    indexed.drop(1).each do |cur|
      if cur[0] - prev[0] <= MAX_CONSECUTIVE_GAP
        prev = cur
      else
        runs << [start, prev]
        start = prev = cur
      end
    end
    runs << [start, prev]

    runs.reverse.map do |s, e|
      _, ts, ys = s
      _, te, ye = e
      if ts == te && ys == ye
        "#{ts} #{ys}"
      else
        "#{ts} #{ys}–#{te} #{ye}"
      end
    end.join(", ")
  end

  def format_week_ranges(weeks)
    return "" if weeks.empty?
    by_year = {}
    weeks.each { |y, w| (by_year[y] ||= []) << w }
    parts = []
    by_year.keys.sort.reverse.each do |year|
      values = by_year[year].uniq.sort
      runs = []
      start = prev = values.first
      values.drop(1).each do |w|
        if w == prev + 1
          prev = w
        else
          runs << [start, prev]
          start = prev = w
        end
      end
      runs << [start, prev]
      runs.reverse.each do |s, e|
        parts << (s == e ? "#{year}, Week #{s}" : "#{year}, Weeks #{s}–#{e}")
      end
    end
    parts.join(", ")
  end

  def teaching_when(entries)
    term_years = entries.select { |e| e["term"] && e["year"] }
                        .map { |e| [e["year"].to_i, e["term"]] }
    weeks = entries.select { |e| e["week"] && e["year"] }
                   .map { |e| [e["year"].to_i, e["week"].to_i] }
    bare_years = entries.select { |e| e["year"] && !e["term"] && !e["week"] }
                        .map { |e| e["year"].to_i }

    return format_term_ranges(term_years) unless term_years.empty?
    return format_week_ranges(weeks) unless weeks.empty?
    return bare_years.uniq.sort.reverse.join(", ") unless bare_years.empty?
    ""
  end

  def merge_group(entries)
    first = entries.first
    seen = {}
    coteachers = []
    entries.each do |e|
      (e["coteachers"] || []).each do |c|
        name = c.is_a?(Hash) ? c["name"] : c
        next if name.nil? || seen[name]
        seen[name] = true
        coteachers << c
      end
    end
    {
      "title" => first["title"],
      "code" => first["code"],
      "inst" => first["inst"],
      "role" => first["role"],
      "coteachers" => coteachers,
      "when" => teaching_when(entries),
      "description" => entries.map { |e| e["description"] }.compact.first,
      "files" => entries.map { |e| e["files"] }.compact.first,
      "year" => first["year"],
      "week" => first["week"],
      "term" => first["term"],
      "_sort" => entries.map { |e| sort_key(e) }.min,
    }
  end

  def merge_teaching(entries)
    by_inst = {}
    entries.each { |e| (by_inst[e["inst"]] ||= []) << e }
    result = {}
    by_inst.each do |inst, inst_entries|
      sub = {}
      order = []
      inst_entries.each do |e|
        key = [e["code"], e["title"]]
        order << key unless sub.key?(key)
        (sub[key] ||= []) << e
      end
      merged = order.map { |k| merge_group(sub[k]) }
      merged.sort_by! { |m| m["_sort"] }
      result[inst] = merged
    end
    result
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  data = site.data["teaching"] || []
  site.data["teaching_merged"] = TeachingMerge.merge_teaching(data)
end
