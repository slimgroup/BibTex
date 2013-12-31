[Wikipedia]: http://en.wikipedia.org/wiki/bibtex
[original manual]: http://ctan.cms.math.ca/tex-archive/biblio/bibtex/base/btxdoc.pdf
# BibTeX Database Documentation

Original Author: Arnold Ip
Some of the code analysis was done entirely by scanning through the code. I did
not find any documentation relating to the code from previous work terms. I
hope this helps you get an understanding of what the code does (there's a
chance you'll read the code again anyway).


Because, clearly, a local version is better.

## What is?

BibTeX is a citation format employed in LaTeX, to simplify the process for
writers (from what I can glean). Basically, the reason we're using BibTeX is
because we're using LaTeX (if we move to Markdown and Pandoc we might be able
to move to a new system).

It uses fairly simple syntax and most of the information about its syntax is
available on [Wikipedia]\ (the original web page is _useless_). There are a few
other PDFs available that go more in depth/are harder to look through. Here's
the [original manual].


## SCons

Basically, the SCons script (the file is SConstruct) is a script that's
syntactically similar to python. It's like a makefile except written in a
python way. That means if there are no changes to the files, it won't run.

### What's in it?

Basically, the SCons script calls a couple of python scripts to run:

1. splitkey.py: it's a verifier and a file merger. If there are
   duplicate keys it'll spew crap at you though. Runs twice. First to
   create the `internal.bib` file and the second time to merge
   `internal.bib` and `external.bib` to create `slimbib.bib`
1. timer.py: Seems this goes and checks the date_submitted entry in the
   `unpublished.bib`. Any entries older than 45 days are sent into the
   error list and emailed to the admin for bibtex.
1. The last part is that it runs the PDF command and converts the files
   to LaTeX and PDF. This process checks for errors in the BibTeX.