---
layout: base
title: Exposition
published: false
---

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
