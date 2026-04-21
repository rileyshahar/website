---
layout: base
title: AMTRaK
---

**AMTRaK** (the **A**tlantic **M**eeting on **T**opology, **R**epresentation
theory, **a**nd **K**-theory) is a day-long seminar aimed at algebraic
topologists working in the mid-Atlantic and Northeast region. We encourage
participants to carpool or travel via train (although Amtrak is not required) to
minimize environmental impact.

This seminar is meant to boost connections within the algebraic topology
community in the mid-Atlantic and Northeast region, particularly amongst
graduate students. Each meeting will focus on a different topic of contemporary
research interest, with two advanced talks in the afternoon and two “pre-talks”
in the morning.

The conference is organized by [Riley Shahar](https://rileyshahar.com) (Penn)
and Nooria Ahmed (Hopkins). Previous organizers include
[Maxine Calle](https://web.sas.upenn.edu/callem/),
[Anish Chedalavada](https://aragogh.github.io/), and
[Ben Spitz](https://benspitz.com/). The conference would not be possible without
the generous support of many people. Supporters of past conferences include
[Nir Gadish](https://www.sas.upenn.edu/~ngadish/), David Gepner, and
[Mona Merling](https://www2.math.upenn.edu/~mmerling/); the Mathematics
Departments at Penn, Hopkins, and UVA; and
[the K-theory foundation](https://sites.unimi.it/ktf/).

<ul>
{%- assign conferences = site.data.amtraks | sort: "date" | reverse -%}
{%- for c in conferences -%}
  <li>{% include amtrak-conference.html conference=c %}</li>
{%- endfor -%}
</ul>
