# Author: G. Hennenfent
#         Seismic Laboratory for Imaging and Modeling
#         Department of Earch & Ocean Sciences
#         The University of British Columbia
#         
# Date  : May, 08

Help("""
Basic tool for extracting, by type, one's contribution(s) from a
BibTeX database

TYPE
"scons -f SConscript author=Lastname"
to extract contributions of Lastname from slimbib.bib to
Lastname(TYPES).bib

"scons -f SConscript author=Lastname iname=my.bib"
to extract contributions of Lastname from my.bib to
Lastname(TYPES).bib

Current types implemented are ARTICLE and CONFERENCE.

EXAMPLE
"scons -f SConscript author=Hennenfent iname=slimbib.bib"

For more complex operations, check bib2bib
(http://www.lri.fr/~filliatr/bibtex2html/doc/#htoc12) part of
bibtex2html (http://www.lri.fr/~filliatr/bibtex2html)
""")

import string as st
import os 

env = Environment(ENV = {'PATH' : os.environ['PATH']})

author = ARGUMENTS.get('author','Hennenfent')
iname  = ARGUMENTS.get('iname','slimbib.bib')

blist  = 'ARTICLE CONFERENCE'

for ptype in st.split(blist):
    oname = author+ptype+'.bib'
    env.Command(oname,iname,
                'scons -Q type=%(ptype)s author=%(author)s oname=%(oname)s iname=%(iname)s'%vars() )
