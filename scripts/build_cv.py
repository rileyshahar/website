#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data"
OUT_TEX = ROOT / "cv" / "cv.tex"

LATEX_SUBS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}

def tex_escape(s: str) -> str:
    return "".join(LATEX_SUBS.get(ch, ch) for ch in s)

def parse_date(x) -> dt.date | None:
    if x is None:
        return None
    if isinstance(x, dt.date):
        return x
    if isinstance(x, str):
        x = x.strip()
        x = x.rstrip("}")  # tolerate the '2024-11-22}' typo
        return dt.date.fromisoformat(x)
    # tolerate yaml numbers/etc.
    return dt.date.fromisoformat(str(x).rstrip("}"))

def load_yaml(name: str):
    return yaml.safe_load((DATA / name).read_text(encoding="utf-8"))

def fmt_month_year(d: dt.date | None) -> str:
    if not d:
        return ""
    return d.strftime("%b %Y")

def fmt_year(d: dt.date | None) -> str:
    if not d:
        return ""
    return d.strftime("%Y")

def render():
    meta = load_yaml("cv.yaml") if (DATA / "cv.yaml").exists() else {}
    papers = load_yaml("papers.yaml") or []
    rtalks = load_yaml("research-talks.yaml") or []
    etalks = load_yaml("expository-talks.yaml") or []
    teaching = load_yaml("teaching.yaml") or []

    # normalize dates
    for p in papers:
        p["date"] = parse_date(p.get("date"))
    for t in rtalks:
        t["date"] = parse_date(t.get("date"))
    for t in etalks:
        t["date"] = parse_date(t.get("date"))

    papers.sort(key=lambda p: p.get("date") or dt.date.min, reverse=True)
    rtalks.sort(key=lambda t: t.get("date") or dt.date.min, reverse=True)
    etalks.sort(key=lambda t: t.get("date") or dt.date.min, reverse=True)

    upenn = [c for c in teaching if c.get("inst") == "University of Pennsylvania"]
    chester = [c for c in teaching if c.get("inst") == "SCI Chester"]
    reed  = [c for c in teaching if c.get("inst") == "Reed College"]
    mc    = [c for c in teaching if c.get("inst") == "Mathcamp"]

    def term_key(term: str) -> int:
        # tweak if you like
        return {"Spring": 0, "Summer": 1, "Fall": 2}.get(term, 99)

    upenn.sort(key=lambda c: (c.get("year", 0), term_key(c.get("term","")), c.get("code","")), reverse=True)
    chester.sort(key=lambda c: (c.get("year", 0), term_key(c.get("term",""))), reverse=True)
    reed.sort(key=lambda c: (c.get("year", 0), term_key(c.get("term","")), c.get("code","")), reverse=True)
    mc.sort(key=lambda c: (c.get("year", 0), int(c.get("week", 0))), reverse=True)

    first = meta.get("first", "Your")
    last = meta.get("last", "Name")
    email = meta.get("email", "")
    website = meta.get("website", "")
    affiliation = meta.get("affiliation", "")

    lines: list[str] = []
    lines += [
r"\documentclass[11pt,letterpaper]{moderncv}",
r"\moderncvstyle{classic}",
r"\moderncvcolor{black}",
r"\usepackage[scale=0.86]{geometry}",
r"\usepackage{hyperref}",
r"\hypersetup{colorlinks=true,urlcolor=blue}",
"",
rf"\name{{{tex_escape(first)}}}{{{tex_escape(last)}}}",
rf"\email{{{tex_escape(email)}}}" if email else "",
rf"\homepage{{{website}}}" if website else "",
rf"\extrainfo{{{tex_escape(affiliation)}}}" if affiliation else "",
"",
r"\begin{document}",
r"\makecvtitle",
"",
r"\section{Publications}",
    ]

    if not papers:
        lines += [r"\cvitem{}{(none yet)}"]
    for p in papers:
        title = tex_escape(p.get("title",""))
        coauthors = p.get("coauthors") or []
        co = ""
        if coauthors:
            co = r" (with " + tex_escape(", ".join(coauthors)) + ")"
        arxiv = p.get("arxiv")
        arxiv_str = str(arxiv).strip() if arxiv is not None else ""
        arxiv_bit = ""
        if arxiv_str:
            arxiv_bit = rf". \href{{https://arxiv.org/abs/{arxiv_str}}}{{arXiv:{arxiv_str}}}"
        status = p.get("status")
        status_bit = rf" \emph{{({tex_escape(str(status))})}}" if status else ""
        year = fmt_year(p.get("date"))
        lines += [rf"\cvitem{{{year}}}{{\emph{{{title}}}{co}{arxiv_bit}{status_bit}}}"]

    lines += [
"",
r"\section{Talks}",
r"\subsection{Research}",
    ]
    for t in rtalks:
        title = tex_escape(t.get("title",""))
        venue = tex_escape(t.get("venue",""))
        when = fmt_month_year(t.get("date"))
        lines += [rf"\cvitem{{{when}}}{{\emph{{{title}}} --- {venue}}}"]

    lines += [
"",
r"\subsection{Expository}",
    ]
    for t in etalks:
        title = tex_escape(t.get("title",""))
        venue = tex_escape(t.get("venue",""))
        when = fmt_month_year(t.get("date"))
        lines += [rf"\cvitem{{{when}}}{{\emph{{{title}}} --- {venue}}}"]

    lines += [
"",
r"\section{Teaching or Course Assisting}",
r"\subsection{University of Pennsylvania}",
    ]
    for c in upenn:
        lines += [rf"\cvitem{{{tex_escape(c.get('term',''))} {c.get('year','')}}}{{{tex_escape(c.get('code',''))}: \emph{{{tex_escape(c.get('title',''))}}}}}"]

    lines += [
"",
r"\subsection{State Correctional Institution Chester}",
    ]
    for c in chester:
        coteachers = c.get("coteachers") or []
        with_bit = ""
        if coteachers:
            with_bit = " (with " + tex_escape(", ".join(coteachers)) + ")"
        lines += [rf"\cvitem{{{tex_escape(c.get('term',''))} {c.get('year','')}}}{{\emph{{{tex_escape(c.get('title',''))}}}{with_bit}}}"]

    lines += [
"",
r"\subsection{Canada/USA Mathcamp}",
    ]
    for c in mc:
        coteachers = c.get("coteachers") or []
        with_bit = ""
        if coteachers:
            with_bit = " (with " + tex_escape(", ".join(coteachers)) + ")"
        lines += [rf"\cvitem{{{c.get('year','')} Week {c.get('week','')}}}{{\emph{{{tex_escape(c.get('title',''))}}}{with_bit}}}"]

    lines += [
"",
r"\subsection{Reed College}",
    ]
    for c in reed:
        lines += [rf"\cvitem{{{tex_escape(c.get('term',''))} {c.get('year','')}}}{{{tex_escape(c.get('code',''))}: \emph{{{tex_escape(c.get('title',''))}}}}}"]

    lines += [
"",
r"\end{document}",
    ]

    OUT_TEX.parent.mkdir(parents=True, exist_ok=True)
    OUT_TEX.write_text("\n".join([ln for ln in lines if ln != ""]), encoding="utf-8")
    print(f"Wrote {OUT_TEX}")

if __name__ == "__main__":
    render()
