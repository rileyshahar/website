---
layout: base
title: Math
---

Some things I am currently thinking about (click to read more---I don't claim
that any of these ideas are either good or original):

<ul>
  <li>
    {% capture crossed_simplicial_groups %}
There are some categorical perspectives on crossed simplicial groups that I
haven't seen explored much; for instance, a crossed simplicial group is a
distributive law between certain monads. Do these perspectives lend any insight
to the classical classification? Can we use them to help with the extension
problem (for instance can we define cohomology of crossed simplicial groups), or
to build a theory of higher crossed simplicial groups?
    {% endcapture %}
    {% include toggle.html
      label="Crossed simplicial groups"
      sr="Toggle details about crossed simplicial groups"
      body=crossed_simplicial_groups
      uid="math-crossed-simplicial-groups"
      quote=1
    %}
  </li>
  <li>
    {% capture parameterized_cohomology %}
It is a folklore observation that $$\text{RO}(G)$$-graded cohomology might be
better thought of as $$\text{Pic}(\text{Sp}_G)$$-graded, so that we don't have
to pick canonical representatives of each representation. (See, for instance,
the discussion at the start of section 6 of
[these notes](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/prerequisites_for_carlsson.pdf)
of Adams.) This might motivate us to try to consider
$$\text{Pic}(\text{Sp}_T)$$-graded cohomology, where $$\text{Sp}_T$$ is the
category of $$T$$-spectra coming from parameterized higher category theory. Is
there a Brown representability theorem for such things, for instance? What do
they look like in the global setting?
    {% endcapture %}
    {% include toggle.html
      label="Parameterized cohomology"
      sr="Toggle details about parameterized cohomology"
      body=parameterized_cohomology
      uid="math-parameterized-cohomology"
      quote=1
    %}
  </li>
  <li>
    {% capture stable_discrete_morse_theory %}
Discrete Morse theory is a powerful toolbox for proving homology equivalences
between CW complexes. Much of the theory seems to me to depend only on the
combinatorics of cells; and for instance, it has been generalized to the
equivariant setting by Freij (although the extension seems far from formal to
me). Can we build an analogous theory for cellular spectra? More generally, can
we identify some categorical description of the settings in which such theories
exist?
    {% endcapture %}
    {% include toggle.html
      label="Stable discrete Morse theory"
      sr="Toggle details about stable discrete Morse theory"
      body=stable_discrete_morse_theory
      uid="math-stable-discrete-morse-theory"
      quote=1
    %}
  </li>
</ul>

I would love to talk about these things or anything
else---[send me an email](mailto:rshahar@sas.upenn.edu)!

## Papers

I'm young and there is not much here yet... but hopefully there will be more
soon!

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

    {%- assign sr = "Toggle abstract for " | append: p.title -%}
    {%- include toggle.html label=label sr=sr body=p.abstract uid=uid quote=1 -%}

  </li>
{%- endfor -%}
</ul>

## Talks

<ul>
{%- assign talks = site.data.research-talks | concat: site.data.expository-talks
  |sort: "date" | reverse -%}
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
    {%- assign sr = "Toggle abstract for " | append: t.title -%}
    {%- include toggle.html label=label sr=sr body=t.abstract uid=uid quote=1 -%}
  </li>
{%- endfor -%}
</ul>

<!-- ## Expository Talks -->
<!---->
<!-- <ul> -->
<!-- {%- assign talks = site.data.expository-talks | sort: "date" | reverse -%} -->
<!-- {%- for t in talks -%} -->
<!--   {%- assign uid = "desc-" | append: t.title | append: "-" | append: t.year | slugify -%} -->
<!--   <li> -->
<!--     {% capture label %} -->
<!--     <em>{{ t.title }}</em> -->
<!--     {%- if t.venue -%} — -->
<!--       {%- if t.venue_url -%} -->
<!--         <a href="{{ t.venue_url }}">{{ t.venue }}</a> -->
<!--       {%- else -%} -->
<!--         {{ t.venue }} -->
<!--       {%- endif -%} -->
<!--       , {{ t.date | date:"%B %Y"  }} -->
<!--     {%- endif -%} -->
<!--     {% endcapture %} -->
<!--     {%- assign sr = "Toggle abstract for " | append: t.title -%} -->
<!--     {%- include toggle.html label=label sr=sr body=t.abstract uid=uid quote=1 -%} -->
<!--   </li> -->
<!-- {%- endfor -%} -->
<!-- </ul> -->
