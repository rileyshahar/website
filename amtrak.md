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

The conference is organized by Riley Shahar (Penn) and Nooria Ahmed (Hopkins).
Past organizers include Maxine Calle, Anish Chedalavada, and Ben Spitz. See
previous editions of the conference on
[Maxine's website](https://web.sas.upenn.edu/callem/amtrak/), from which the
conference description is shamelessly stolen.

<ul>
{%- assign conferences = site.data.amtraks | sort: "date" | reverse -%}
{%- for c in conferences -%}
  <li>{% include amtrak-conference.html conference=c %}</li>
{%- endfor -%}
</ul>
