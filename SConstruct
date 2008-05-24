# Author: G. Hennenfent
#         Seismic Laboratory for Imaging and Modeling
#         Department of Earch & Ocean Sciences
#         The University of British Columbia
#         
# Date  : May, 08

Help("""
Basic tool for extracting some entries from a BibTeX database.

TYPE
"scons author=lastname"
to extract publications by lastname from slimbib.bib to res.bib

"scons year=YYYY"
to extract publications of year YYYY from slimbib.bib to res.bib

"scons kwd=keyword"
to extract publications containing keyword from slimbib.bib to res.bib

"scons year=YYYY oname=filename.bib"
to extract publications of year YYYY from slimbib.bib to filename.bib

"scons year=YYYY iname=fname1.bib oname=fname2.bib"
to extract publications of year YYYY from fname1.bib to fname2.bib

EXAMPLES
"scons year=2004"
"scons author=Hennenfent year=2004"
"scons kwd=SLIM"
"scons kwd=SLIM oname=slimstuff.bib"

For more complex operations, check bib2bib
(http://www.lri.fr/~filliatr/bibtex2html/doc/#htoc12) part of
bibtex2html (http://www.lri.fr/~filliatr/bibtex2html)
""")

author = ARGUMENTS.get('author','all')
kwd    = ARGUMENTS.get('kwd','all')
ptype  = ARGUMENTS.get('type','all')

year   = int(ARGUMENTS.get('year',0))

iname  = ARGUMENTS.get('iname','slimbib.bib')
oname  = ARGUMENTS.get('oname','res.bib')

cond = ''
if author is not 'all':
    cond = cond+'''-c 'author : "%s" ' '''%author
if year is not 0:
    cond = cond+'''-c 'year=%d' '''%year
if kwd is not 'all':
    cond = cond+'''-c 'keywords : "%s" ' '''%kwd
if ptype is not 'all':
    cond = cond+'''-c '$$type="%s" ' '''%ptype

Command(oname,iname,
        'bib2bib -ob $TARGET $SOURCE '+cond)
