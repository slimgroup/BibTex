# Author: G. Hennenfent
#         Seismic Laboratory for Imaging and Modeling
#         Department of Earch & Ocean Sciences
#         The University of British Columbia
#         
# Date  : May, 08

Help("""
Basic tool for extracting some entries from slimbib.bib.

Type "scons author=lastname" to extract publications by lastname
     "scons year=YYYY"       to extract publications of year YYYY
     "scons kwd=keyword"     to extract publications containing keyword

The extracted publications are in res.bib.

Examples:
     "scons year=2004"
     "scons author=Hennenfent year=2004"
     "scons kwd=SLIM"

For more complex operations, check bib2bib
(http://www.lri.fr/~filliatr/bibtex2html/doc/#htoc12) part of
bibtex2html (http://www.lri.fr/~filliatr/bibtex2html)
""")

author = ARGUMENTS.get('author','all')
year   = int(ARGUMENTS.get('year',0))
kwd    = ARGUMENTS.get('kwd','all')

bibfile = 'slimbib.bib'

cond = ''
if author is not 'all':
    cond = cond+'''-c 'author : "%s" ' '''%author
if year is not 0:
    cond = cond+'-c year=%d '%year
if kwd is not 'all':
    cond = cond+'''-c 'keywords : "%s" ' '''%kwd

Default(Command('res.bib',bibfile,
                'bib2bib -ob $TARGET $SOURCE '+cond))

Command('ghennenfent.bib',bibfile,
        '''bib2bib -ob $TARGET $SOURCE  -c 'author : "Hennenfent" ' ''')
