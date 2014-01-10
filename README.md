[Wikipedia]: http://en.wikipedia.org/wiki/bibtex
[original manual]: http://ctan.cms.math.ca/tex-archive/biblio/bibtex/base/btxdoc.pdf
# BibTeX Database Documentation

Original Author: Arnold Ip
Some of the code analysis was done entirely by scanning through the code. I did
not find any documentation relating to the _code_ from previous work terms. I
hope this helps you get an understanding of what the code does (there's a
chance you'll read the code again anyway).

If you have any questions, or find things unclear, feel free to email Arnold to
clarify. Ask for his email as he doesn't want to get spammed. Henryk should
know it ;)

**Why was this written?** Because, clearly, a local version is better.
There will likely be a post with all this information on iSLIM. Please first
make changes here first, then export to HTML and 

## What each file is (Shruti's README)

- `internal.bib`  - internal SLIM's publications
- `external.bib`  - external publications cited by SLIM
- `slimbib.bib`   - internal and external combined using SConstruct
		  run scons in this directory to recreate it


USAGE------------------------
1. Add internal citations in the corresponding bibtex type file, for eg: Add a journal paper entry in file "article.bib", etc... 
2. Add external citations in the file external.bib
3. Run scons to merge the above two files simply by typing 'scons' in command line
4. In order to compare two or more .bib files, edit SConstruct in the following format:
   `Command('$TARGET',['$SOURCEFILE1','$SOURCEFILE2'],'python splitkey.py output input1 input2' )`
5. If duplicate keys are found, edit them and repeat step 3



## What is BibTeX?

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
   
### What can be changed in the scripts?

In SConstruct file, it'd probably be beneficial to try and make it
more usable by making the input in the `command()` functions more
understandable. You can do this by using a variable to specify the input
parameters (right now it's like repeating yourself and having to change both
variables).

I put down some notes in the scripts. We can sorta reduce the lines and use
regex to extract the content, but realistically the code there's probably (?)
more readable. Though, I suppose that's arguable.

### Some other scripts that are here

- Two scripts that are separate from the scons script.
- Used mainly as maintenance scripts:

2. urlcheck.py: uses a regular expression to look for URLs in entries in order
   to make sure they work. Assumes that the URLs are stored in specific values
   within each entry. running this script takes a while so probably only need
   to run it once in a while. Output is printed to urlerror.txt.
   Code was originally based off of `splitkey.py` but definitely can be
   refactored.
   
   Usage: `python urlcheck.py $outputfile $bibfile1 $inputfile2 etc`

   The output file is a successful merged \\(\BiBTeX{}\\) file of the input
2. month_conversion.py: runs through the input files to convert all month types
   to double-digit months. This is for use in sorting SLIM's web page (which,
   for some reason, still doesn't sort properly). That's fine though. At least
   the \\(\BiBTeX{}\\) is consistent.

   Usage: `python month_conversion.py $input1 $input2 etc`
2. multicheck.py: It was originally created to do _everything_ but when it was
   realized that it was a stupid idea it was scrapped. Forgot to delete.

   Usage: don't use it.

