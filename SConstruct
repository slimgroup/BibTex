# Author: G. Hennenfent
#         Seismic Laboratory for Imaging and Modeling
#         Department of Earch & Ocean Sciences
#         The University of British Columbia
#         
# Date  : May, 08

author = ARGUMENTS.get('author','all')
year   = ARGUMENTS.get('year','all')
group  = ARGUMENTS.get('group','all')
ptype  = ARGUMENTS.get('ptype','all')

cond = ''
if author is not 'all':
    cond = '''-c 'author : "%s" ' '''%author
if year is not 'all':
    cond = '-c "year=%d'%year

Command('res.bib','slimbib.bib','bib2bib -ob $TARGET $SOURCE '+cond)
