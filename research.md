---
layout: base
title: Research
---

I'm young and there is not much here yet... but hopefully there will be more
soon!

### Research Papers

<ul>
{%- assign papers = site.data.papers | sort: "date" | reverse -%}
{%- for p in papers -%}
  {%- assign uid = "desc-" | append: c.title | append: "-" | append: c.year | slugify -%}
  <li>
    <em>{{ p.title }}</em>
    {%- if p.coauthors and p.coauthors.size > 0 -%}
      , with {{ " " }}
      {%- assign list=p.coauthors -%}
      {%- include comma-sep.html list=list -%}
    {%- endif -%}
    {%- if p.arxiv %} — <a href="https://arxiv.org/abs/{{ p.arxiv }}" target="_blank">arXiv:{{ p.arxiv }}</a>{% endif -%}
    {%- if p.status %} ({{ p.status }}){% endif -%}

    {%- if p.abstract -%}
      {%- assign sr = "Show abstract of " | append: p.title -%}
      {%- include toggle.html sr=sr body=p.abstract uid=uid markdown=1 -%}
    {%- endif -%}
  </li>
{%- endfor -%}
</ul>

### Research Talks

<ul>
{%- assign talks = site.data.research-talks | sort: "date" | reverse -%}
{%- for t in talks -%}
  {%- assign uid = "desc-" | append: t.title | append: "-" | append: t.year | slugify -%}
  <li>
    <em>{{ t.title }}</em>
    {%- if t.venue -%} —
      {%- if t.venue_url -%}
        <a href="{{ t.venue_url }}" target="_blank">{{ t.venue }}</a>
      {%- else -%}
        {{ t.venue }}
      {%- endif -%}
      , {{ t.date | date:"%B %Y"  }}
    {%- endif -%}
    {%- if t.abstract -%}
      {%- assign sr = "Show abstract of " | append: t.title -%}
      {%- include toggle.html sr=sr body=t.abstract uid=uid markdown=1 -%}
    {%- endif -%}
  </li>
{%- endfor -%}
</ul>

### Expository Talks

<ul>
{%- assign talks = site.data.expository-talks | sort: "date" | reverse -%}
{%- for t in talks -%}
  {%- assign uid = "desc-" | append: t.title | append: "-" | append: t.year | slugify -%}
  <li>
    <em>{{ t.title }}</em>
    {%- if t.venue -%} —
      {%- if t.venue_url -%}
        <a href="{{ t.venue_url }}" target="_blank">{{ t.venue }}</a>
      {%- else -%}
        {{ t.venue }}
      {%- endif -%}
      , {{ t.date | date:"%B %Y"  }}
    {%- endif -%}
    {%- if t.abstract -%}
      {%- assign sr = "Show abstract of " | append: t.title -%}
      {%- include toggle.html sr=sr body=t.abstract uid=uid markdown=1 -%}
    {%- endif -%}
  </li>
{%- endfor -%}
</ul>
