# Author: G. Hennenfent
#         Seismic Laboratory for Imaging and Modeling
#         Department of Earch & Ocean Sciences
#         The University of British Columbia
#         
# Date  : May, 08

import string as st
import os 

env = Environment(ENV = {'PATH' : os.environ['PATH']})

author = ARGUMENTS.get('author','Hennenfent')

blist = 'ARTICLE CONFERENCE'

for ptype in st.split(blist):
    fname = author+ptype+'.bib'
    env.Command(fname,'slimbib.bib',
                'scons -Q type=%(ptype)s author=%(author)s fname=%(fname)s'%vars() )
