internal.bib	- internal SLIM's publications
external.bib	- external publications cited by SLIM
slimbib.bib	- internal and external combined using SConstruct
		  run scons in this directory to recreate it


USAGE------------------------
1. Add internal citations in the file internal.bib
2. Add external citations in the file external.bib
3. Run scons to merge the above two files simply by typing 'scons' in command line
4. In order to compare two or more .bib files, edit SConstruct in the following format:
Command('$TARGET',['$SOURCEFILE1','$SOURCEFILE2'],'python splitkey.py output input1 input2' )

5. If duplicate keys are found, edit them and repeat step 3
