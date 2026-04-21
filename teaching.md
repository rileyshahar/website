---
layout: base
title: Teaching
---

I love to teach.

## Penn

I TA at Penn some semesters of the academic year.

<ul>
{%- assign upenn = site.data.teaching | where: "inst", "University of Pennsylvania" -%}
{%- assign years = upenn | map: "year" | uniq | sort | reverse -%}
{%- assign term_order = "Fall,Spring" | split: "," -%}

{%- for y in years -%} {%- for term in term_order -%}
{%- assign subset = upenn | where: "year", y | where: "term", term -%}
{%- for c in subset -%} <li> {{ c.term }} {{ c.year }} — {{ c.code }}:
<em>{{ c.title }}</em> </li> {%- endfor -%} {%- endfor -%} {%- endfor -%}

</ul>

## SCI Chester

In Spring 2026, I cotaught a pilot workshop with three other Penn graduate
students at State Correctional Institution Chester.

<ul>
{%- assign chester = site.data.teaching | where: "inst", "SCI Chester" -%}
{%- assign years = chester | map: "year" | uniq | sort | reverse -%}
{%- assign term_order = "Fall,Spring" | split: "," -%}

{%- for y in years -%} {%- for term in term_order -%}
{%- assign subset = chester | where: "year", y | where: "term", term -%}
{%- for c in subset -%} <li> {{ c.term }} {{ c.year }} — <em>{{ c.title }}</em>
{%- if c.coteachers and c.coteachers.size > 0 -%} , with {{ " " }}
{%- include comma-sep.html list=c.coteachers -%} {%- endif -%} </li>
{%- endfor -%} {%- endfor -%} {%- endfor -%}

</ul>

## Mathcamp

Teaching at [Mathcamp](https://mathcamp.org) is a unique experience. Over the
course of a summer, a Mathcamp instructor designs and teaches (approximately)
five (approximately) weeklong courses on subjects of their choosing, targeted
towards extremely motivated high-school-aged students. I would be super excited
to talk with anyone about the pedagogical choices behind any of these classes,
as well as to share content and discuss things I would change :).

<ul>
{%- assign mathcamp = site.data.teaching | where: "inst", "Mathcamp" -%}
{%- assign years = mathcamp | map: "year" | uniq | sort | reverse -%}
{%- assign weeks = "1,2,3,4,5" | split: "," -%}

{%- for y in years -%} {%- for week in weeks -%}
{%- assign subset = mathcamp | where: "year", y | where: "week", week -%}
{%- for c in subset -%}
{%- assign uid = "desc-" | append: c.title | append: "-" | append: c.year | append: "-" | append: c.week | slugify -%}

<li>
    {% capture label %}
    {{ c.year }} Week {{ c.week }} — <em>{{ c.title }}</em>
{%- if c.coteachers and c.coteachers.size > 0 -%} , with {{ " " }}
{%- include comma-sep.html list=c.coteachers -%} {%- endif -%} {% endcapture %}
{%- assign sr = "Toggle description for " | append: c.title -%}
{%- include toggle.html label=label sr=sr body=c.description uid=uid quote=1 -%}

</li> {%- endfor -%} {%- endfor -%} {%- endfor -%}

</ul>

## Reed

Course-assisting at Reed consists of grading, holding office hours, and being an
intermediary between the students and professor.

<ul>
{%- assign reed = site.data.teaching | where: "inst", "Reed College" -%}
{%- assign years = reed | map: "year" | uniq | sort | reverse -%}
{%- assign term_order = "Fall,Spring" | split: "," -%}

{%- for y in years -%} {%- for term in term_order -%}
{%- assign subset = reed | where: "year", y | where: "term", term -%}
{%- for c in subset -%} <li> {{ c.term }} {{ c.year }} — {{ c.code }}:
<em>{{ c.title }}</em> </li> {%- endfor -%} {%- endfor -%} {%- endfor -%}

</ul>
