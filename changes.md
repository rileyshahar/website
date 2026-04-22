1. Dates like "2025-26" aren't formatted properly, something is swallowing the
   dash.
2. Dates can be split across multiple lines---if there is not enough room to fit
   a date on a line, th entire date should appear on the line underneath,
   overlapping vertically with the CV item. (For instance, this happens with the
   saturated transfer systems talk and the REPL REU.)
3. There should be a link to the expository paper.
4. It should be possible to use the script to build it locally without needing
   to install the whole latex toolchain, which tectonic is currently doing. Keep
   the behavior of not leaving around any build artificats.
5. When I TA'd for the same class multiple times, they should be groups
   together. (You should do this automatically from the script, rather than in
   the YAML.)
6. Service like the Penn Graduate Pizza Seminar, Reed Math Student Colloquium,
   etc. should be formatted with the name and then the venue, e.g.
   "**Co-organizer**, Graduate Pizza Seminar, University of Pennsylvania, with
   Chris Dunstan"
7. Under education, Penn should list my GRFP, and Reed should list Phi Beta
   Kappa. Penn should also list my oral exam under Mona Merling and Nir Gadish
   on parameterized higher category theory. See `cv-examples/cv-calle.pdf` for
   how I think the visual hierarchy in the education section should work.
