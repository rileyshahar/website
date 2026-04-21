# Structural changes for the site

This is my Jekyll academic website. Please make the structural and technical
changes below.

**Do not write or rewrite any prose content** — no paragraphs, no abstracts, no
bios, no descriptions, no page-title rewording. Every change below is a template
edit, CSS adjustment, file move/delete, config change, or a one-token link/label
addition. If any change would require authoring prose, skip it and flag it to
me.

Also **do not write any javascript.** This is an html-and-css-only site.

Work through the groups in order. After each group, rebuild with
`bundle exec jekyll build` and confirm the site still renders. You will need to
run `chruby ruby-3.4.1` for the `bundle` command to work.

## 1. Base layout (`_layouts/base.html`)

- Add `lang="en"` to the `<html>` tag.
- Add `<meta name="viewport" content="width=device-width, initial-scale=1">`.
- Add
  `<meta name="description" content="{{ page.description | default: site.description }}">`.
- Add Open Graph + Twitter Card tags driven by page/site variables:
  - `og:title` (page title, falling back to site title)
  - `og:description` (page description, falling back to site description)
  - `og:url` (page absolute URL)
  - `og:image` (default `/assets/images/profile.png`, absolute URL)
  - `og:type` = `website`
  - `twitter:card` = `summary`
- Add `<link rel="canonical" href="{{ page.url | absolute_url }}">`.
- Add `<link rel="icon" href="/favicon.ico">`.
- Remove the Bootstrap CDN `<link>` (we're replacing Bootstrap — see section 2).
- In the navbar loop, add `aria-current="page"` to the active `<li>` (or inner
  element) when `item.url == page.url`. Keep the existing italic/accent styling.
- In the footer, point the "Last updated" link at the repo's commit history
  (`{{ site.repo }}/commits/main`) rather than the repo root. Keep the date text
  identical.

## 2. Bootstrap removal

Bootstrap is currently used only for: `container`, `row`, `col-md-12`, `d-flex`,
`justify-content-between`, `align-items-end`, `list-inline`, `list-inline-item`,
`mb-0`, `text-center`.

Replace it as follows:

- In `_sass/main.scss`, define a `.container` rule (max-width ~960px, horizontal
  auto margin, modest side padding).
- In `_layouts/base.html` (and anywhere else the utility classes appear —
  `404.html`, `_includes/amtrak-conference.html`), **prefer renaming the markup
  to semantic class names** (e.g. `header .nav`, `footer .credits`) and adding
  the corresponding rules in `_sass/main.scss`, rather than porting the utility
  classes one-for-one.
- Once nothing references Bootstrap, delete the Bootstrap CDN `<link>` from the
  head.

Keep the visual result as close to identical as reasonable.

## 3. Navbar (`_data/navbar.yaml`)

Add an AMTRaK entry after Teaching:

```yaml
- title: AMTRaK
  url: /amtrak.html
```

## 4. Toggle accessibility (`_sass/toggle.scss`)

- Replace the `.toggle` off-screen hiding (`left: -9999px`) with a clip-based
  hide that avoids the scroll-on-focus jump. Reuse the same recipe already
  present in `.sr-only`:

  ```
  position: absolute;
  width: 1px;
  height: 1px;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
  ```

- Add a keyboard focus style on the visible toggle head when the hidden checkbox
  is focused:

  ```
  .toggle:focus-visible ~ .toggle-head .toggle-title {
    outline: 2px solid $accent;
    outline-offset: 2px;
  }
  ```

  (Move `$accent` into a shared SCSS module or duplicate it — whichever is
  simpler.)

- Add a `@media (prefers-reduced-motion: reduce)` block that neutralizes any
  transitions introduced during this work.

## 5. Split talks on `math.md`

Currently `math.md` concatenates `site.data.research-talks` and
`site.data.expository-talks` under a single `## Talks` heading. Split into two:

- `## Research talks` — render from `site.data.research-talks`.
- `## Expository talks` — render from `site.data.expository-talks`.

Reuse the existing `for t in talks` Liquid block with the toggle include —
duplicate it per data source; don't change how individual talks render.

Also delete the large commented-out "Expository Talks" block at the bottom of
`math.md` (currently lines 126–148).

These two subsection headings ("Research talks" / "Expository talks") are the
only prose-like strings you should introduce.

## 6. Mathcamp handout links (`teaching.md`)

Several Mathcamp entries in `_data/teaching.yaml` already have a `files:` field
(e.g. `files: extra-stretchy-rubber-sheet-geometry`). The corresponding handout
PDFs live at `assets/<files>/*.pdf` but aren't linked anywhere.

Extend the data schema to accept an optional `handouts` list per entry:

```yaml
handouts:
  - hw1.pdf
  - hw2.pdf
```

Update the Mathcamp loop in `teaching.md` so that when a course has `handouts`
set, it renders a compact inline list of PDF links after the title: one link per
handout, pointing at `/assets/{{ c.files }}/{{ handout }}`. Keep the markup
minimal — plain `<a>` tags separated by commas or a small `<ul>` is fine, your
call.

**Do not populate `handouts` in the YAML for me.** Only make the template
capable of rendering them; I'll fill in the data.

## 7. Responsive profile image (`_sass/main.scss`)

`.profile` currently uses `width: 400px`. Make it responsive:

- ≥ 700px viewport: keep the float-right layout, cap at `max-width: 40%`.
- < 700px viewport: drop the float, center the image, cap at `max-width: 60%`.

## 8. Footer contrast (`_sass/main.scss`)

Remove the `opacity: 0.5` on the `footer` and set an explicit text color that
meets WCAG AA on the `#faf7f2` background (~`#595959` or darker). Keep the rest
of the footer styling unchanged.

## 9. Sitemap and robots.txt

- Add `jekyll-sitemap` to the `Gemfile` (inside the `:jekyll_plugins` group) and
  to the `plugins` list in `_config.yml`.
- Add a `robots.txt` at the site root that points at
  `https://rileyshahar.com/sitemap.xml`.

## 10. CV pipeline in CI (`.github/workflows/jekyll.yml`)

Currently the workflow only builds Jekyll. Add steps **before**
`bundle exec jekyll build`:

1. Set up Python (use 3.14 if the action supports it; otherwise the nearest
   available — flag to me if you have to downgrade).
2. Install `pyyaml` (either via Poetry or directly — direct `pip install pyyaml`
   is fine).
3. Run `python scripts/build_cv.py` to regenerate `cv/cv.tex` from YAML.
4. Compile `cv/cv.tex` → `cv/cv.pdf` using `xu-cheng/latex-action@v3` (or
   equivalent) with `latexmk -pdf`.
5. Copy the resulting PDF to `assets/cv.pdf` so Jekyll picks it up.

Then add the single sentence `Here is my [CV](assets/cv.pdf).` in the paragraph
in `index.md` starting `You can contact me...` That's the only content addition
in this group — no surrounding prose.

## 11. Base font size (`_sass/main.scss`)

Change the `body` rule from `font-size: 1.5rem` to `font-size: 1.125rem`. Verify
H1 (`calc(1.875rem + 1.5vw)`) still looks balanced; adjust only if clearly
broken by the smaller base.

## Verification

Before reporting done:

- `bundle exec jekyll build` with no errors or warnings.
- Spot-check rendered pages: homepage, `math.html` (research + expository
  sections), `teaching.html` (handouts render when present, silent when absent),
  `amtrak.html` (reachable from navbar), `404.html` still styled.
- View-source on one page and confirm: `<html lang="en">`, viewport meta,
  og/twitter tags, canonical link, favicon link, no `bootstrap.min.css`
  reference, `aria-current="page"` on the current nav item.
- Run Lighthouse or axe against the homepage and confirm no _new_ accessibility
  violations.
- `sitemap.xml` present in `_site/` after build; `robots.txt` present.

If anything on this list is ambiguous or would require authoring prose to
complete cleanly, stop and ask.
