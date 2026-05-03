---
layout: base
title: Teaching
---

I love to teach.

## Penn

I TA at Penn some semesters of the academic year.

<ul>
{%- assign upenn = site.data.teaching_merged["University of Pennsylvania"] -%}
{%- for c in upenn -%}
<li> {{ c.when }} — {{ c.code }}: <em>{{ c.title }}</em> </li>
{%- endfor -%}
</ul>

## SCI Chester

In Spring 2026, I cotaught a pilot workshop with three other Penn graduate
students at State Correctional Institution Chester.

<ul>
{%- assign chester = site.data.teaching_merged["State Correctional Institution Chester"] -%}
{%- for c in chester -%}
<li> {{ c.when }} — <em>{{ c.title }}</em>
{%- if c.coteachers and c.coteachers.size > 0 -%} , with {{ " " }}
{%- include comma-sep.html list=c.coteachers -%} {%- endif -%} </li>
{%- endfor -%}
</ul>

## Mathcamp

Teaching at [Mathcamp](https://mathcamp.org) is a unique experience. Over the
course of a summer, a Mathcamp instructor designs and teaches (approximately)
five (approximately) weeklong courses on subjects of their choosing, targeted
towards extremely motivated high-school-aged students. I would be super excited
to talk with anyone about the pedagogical choices behind any of these classes,
as well as to share content and discuss things I would change :).

<ul>
{%- assign mathcamp = site.data.teaching_merged["Canada/USA Mathcamp"] -%}
{%- for c in mathcamp -%}
{%- assign uid = "desc-" | append: c.title | slugify -%}

<li>
    {% capture label %}
    {{ c.when }} — <em>{{ c.title }}</em>
{%- if c.coteachers and c.coteachers.size > 0 -%} , with {{ " " }}
{%- include comma-sep.html list=c.coteachers -%} {%- endif -%} {% endcapture %}
{%- assign sr = "Toggle description for " | append: c.title -%}
{%- include toggle.html label=label sr=sr body=c.description uid=uid quote=1 -%}

</li> {%- endfor -%}

</ul>

## Reed

Course-assisting at Reed consists of grading, holding office hours, and being an
intermediary between the students and professor.

<ul>
{%- assign reed = site.data.teaching_merged["Reed College"] -%}
{%- for c in reed -%}
<li> {{ c.when }} — {{ c.code }}: <em>{{ c.title }}</em> </li>
{%- endfor -%}
</ul>
