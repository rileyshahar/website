---
layout: base
title: Research
published: false
---

I'm young and there is not much here yet... but hopefully there will be more
soon!

## Research Papers

<ul>
{%- assign papers = site.data.papers | sort: "date" | reverse -%}
{%- for p in papers -%}
  {%- assign uid = "desc-" | append: p.title | append: "-" | append: p.year | slugify -%}
  <li>
    {% capture label %}
    <em>{{ p.title }}</em>
    {%- if p.coauthors and p.coauthors.size > 0 -%}
      , with {{ " " }}
      {%- assign list=p.coauthors -%}
      {%- include comma-sep.html list=list -%}
    {%- endif -%}
    {%- if p.arxiv %} — <a href="https://arxiv.org/abs/{{ p.arxiv }}">arXiv:{{ p.arxiv }}</a>{% endif -%}
    {%- if p.status %} ({{ p.status }}){% endif -%}
    {% endcapture %}

    {%- assign sr = "Show abstract of " | append: p.title -%}
    {%- include toggle.html label=label sr=sr body=p.abstract uid=uid quote=1 -%}

  </li>
{%- endfor -%}
</ul>

## Research Talks

<ul>
{%- assign talks = site.data.research-talks | sort: "date" | reverse -%}
{%- for t in talks -%}
  {%- assign uid = "desc-" | append: t.title | append: "-" | append: t.year | slugify -%}
  <li>
    {% capture label %}
    <em>{{ t.title }}</em>
    {%- if t.venue -%} —
      {%- if t.venue_url -%}
        <a href="{{ t.venue_url }}">{{ t.venue }}</a>
      {%- else -%}
        {{ t.venue }}
      {%- endif -%}
      , {{ t.date | date:"%B %Y"  }}
    {%- endif -%}
    {% endcapture %}
    {%- assign sr = "show abstract of " | append: t.title -%}
    {%- include toggle.html label=label sr=sr body=t.abstract uid=uid quote=1 -%}
  </li>
{%- endfor -%}
</ul>

## Expository Talks

<ul>
{%- assign talks = site.data.expository-talks | sort: "date" | reverse -%}
{%- for t in talks -%}
  {%- assign uid = "desc-" | append: t.title | append: "-" | append: t.year | slugify -%}
  <li>
    {% capture label %}
    <em>{{ t.title }}</em>
    {%- if t.venue -%} —
      {%- if t.venue_url -%}
        <a href="{{ t.venue_url }}">{{ t.venue }}</a>
      {%- else -%}
        {{ t.venue }}
      {%- endif -%}
      , {{ t.date | date:"%B %Y"  }}
    {%- endif -%}
    {% endcapture %}
    {%- assign sr = "Show abstract of " | append: t.title -%}
    {%- include toggle.html label=label sr=sr body=t.abstract uid=uid quote=1 -%}
  </li>
{%- endfor -%}
</ul>
