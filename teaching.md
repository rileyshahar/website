---
layout: base
title: Teaching
---

I TA at Penn during the academic year and teach at
[Mathcamp](https://mathcamp.org){:target="_blank"} during summers. In undergrad,
I was a regular course assistant for math and CS courses.

### At Penn

<ul>
{%- assign upenn = site.data.teaching | where: "inst", "University of Pennsylvania" -%}
{%- assign years = upenn | map: "year" | uniq | sort | reverse -%}
{%- assign term_order = "Fall,Spring" | split: "," -%}

{%- for y in years -%}
  {%- for term in term_order -%}
    {%- assign subset = upenn | where: "year", y | where: "term", term -%}
    {%- for c in subset -%}
      <li> {{ c.term }} {{ c.year }} — {{ c.code }}: <em>{{ c.title }}</em> </li>
    {%- endfor -%}
  {%- endfor -%}
{%- endfor -%}
</ul>

### At Mathcamp

Teaching at Mathcamp is a unique experience. Over the course of a summer, a
Mathcamp instructor designs and teaches (approximately) five (approximately)
weeklong courses on subjects of their choosing, targeted towards extremely
motivated high-school-aged students. I would be super excited to talk with
anyone about the pedagogical choices behind any of these classes, as well as to
share content and discuss things I would change :).

<ul>
{%- assign mathcamp = site.data.teaching | where: "inst", "Mathcamp" -%}
{%- assign years = mathcamp | map: "year" | uniq | sort | reverse -%}
{%- assign weeks = "1,2,3,4,5" | split: "," -%}

{%- for y in years -%}
  {%- for week in weeks -%}
    {%- assign subset = mathcamp | where: "year", y | where: "week", week -%}
    {%- for c in subset -%}
      {%- assign uid = "desc-" | append: c.title | append: "-" | append: c.year | append: "-" | append: c.week | slugify -%}
      <li>
        {{ c.year }} Week {{ c.week }} — <em>{{ c.title }}</em>
        {%- if c.coteachers and c.coteachers.size > 0 -%}
					, with {{ " " }}
          {%- include comma-sep.html list=c.coteachers -%}
        {%- endif -%}
        {%- if c.description -%}
          {%- assign sr = "Show description of " | append: c.title -%}
          {%- include toggle.html sr=sr body=c.description uid=uid -%}
        {%- endif -%}
      </li>
    {%- endfor -%}
  {%- endfor -%}
{%- endfor -%}
</ul>

### At Reed

Course-assisting at Reed consists of grading, holding office hours, and being an
intermediary between the students and professor.

<ul>
{%- assign reed = site.data.teaching | where: "inst", "Reed College" -%}
{%- assign years = reed | map: "year" | uniq | sort | reverse -%}
{%- assign term_order = "Fall,Spring" | split: "," -%}

{%- for y in years -%}
  {%- for term in term_order -%}
    {%- assign subset = reed | where: "year", y | where: "term", term -%}
    {%- for c in subset -%}
      <li> {{ c.term }} {{ c.year }} — {{ c.code }}: <em>{{ c.title }}</em> </li>
    {%- endfor -%}
  {%- endfor -%}
{%- endfor -%}
</ul>
