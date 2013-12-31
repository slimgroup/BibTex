
#!/usr/bin/python

import re
import os
import sys


#---------------STANDARD DEFINITIONS----------
entrytypes=["@article{",
		"@conference{",
                "@presentation{",
		"@techreport{",
		"@manual{",
		"@book{",
		"@booklet{",
		"@inbook{",
		"@inproceedings{",
		"@proceedings{",
		"@unpublished{",
		"@submitted{",
		"@inpress{", 
		"@mastersthesis{",
		"@phdthesis{",
		"@incollection{",
		"@misc{"]

#--------------------DECLARATIONS------------

num_files=len(sys.argv)
input_files=[]
setlist=[]

#--------------------------------------------

#CHECKING NUMBER OF FILES
if (num_files <= 3):
	print "Enter command in following format: python splitkey.py outputfile inputfile1.bib inputfile2.bib etc"
        quit()

else:
	print "Reading..."
        output=sys.argv[1]
	i=2
        while i < num_files:
                input_files.append(sys.argv[i])
                i=i+1	

#--------------Working on input files---------
	for each in input_files:
		int_keys=set()
		f=0
		for line in open(each):
			line=line.strip()
			for list in entrytypes:
	            ''' Arnold note: This could probably be done as a regex '''
				if re.search(list.lower(),line.lower(),re.I):
					entries= line.split('@')
					entry=entries[1].strip()
					split_entry= entry.split("{")[1]
					key=split_entry.split(",")[0]
					if key in int_keys:
						print "Error: The key", key, " already exists in file",each,".Not added again.Edit it and try again"
						quit()
					int_keys.add(key)						
		setlist.append(int_keys)
#----------Checking for duplicate keys between files----------
	length=len(setlist)
	j=0
	while j < length:
		set1=setlist[j]
		k=j+1
		while k <= length-1:
			set2=setlist[k]		
			common=set1 & set2
			if len(common) ==0:
				k=k+1
			else:
				print "Duplicate entry found",common
				print "Write failed"
				quit()
		j=j+1	
	fout=open(output,"w")
	for each in input_files:
		for line in open(each):
			fout.write(line)
		print "File" ,each, "copied successfully to ", output 	
		 
	fout.close()
		
