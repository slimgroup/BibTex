

import string as st
import os

env = Environment(ENV = os.environ)
Command('internal.bib', ['conference.bib', 'presentation.bib', 'bscthesis.bib','masterthesis.bib','techreport.bib','unpublished.bib', 'book.bib','article.bib','manual.bib','phdthesis.bib','booklet.bib','inbook.bib','incollection.bib','misc.bib','proceedings.bib'] , 'python3 splitkey.py internal.bib conference.bib bscthesis.bib presentation.bib  masterthesis.bib techreport.bib unpublished.bib book.bib article.bib manual.bib phdthesis.bib booklet.bib inbook.bib incollection.bib misc.bib proceedings.bib')


Command('slimbib.bib',['internal.bib','external.bib'],'python3 splitkey.py slimbib.bib internal.bib external.bib')

Command(' ','unpublished.bib','python3 timer.py unpublished.bib')
pdfOutput = env.PDF(target='referencecheck.pdf',source='referencecheck.tex')
Depends(pdfOutput,Split('referencecheck.tex slimbib.bib'))
