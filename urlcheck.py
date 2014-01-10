
#!/usr/bin/python

import re
import os
import sys
from urllib2 import Request, urlopen, URLError

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

# subentries that contain URL (sometimes the DOI does as well, but there's only one such instance where it actually has "http(s)://". Better to just test that separately because 99% of doi entries don't have it.)
# the \d's are for "more" url types (url, url2, url3, bdsk-url-1, bdsk-url-2). the others don't need it.
urlcontainers = [r'url\d*\s*?=',
        r'bdsk-url-\d\s*?=',
        r'presentation\s*?=',
        r'pdf\s*?=',
        r'file\s*?=',
        r'html_version\s*?='
]

#--------------------DECLARATIONS------------

num_files=len(sys.argv)
input_files=[]
setlist=[]

#--------------------------------------------

#CHECKING NUMBER OF FILES
print sys.argv

if (num_files <= 3):
    print "Enter command in following format: python urlcheck.py outputfile inputfile1.bib inputfile2.bib etc"
    quit()

else:
    print "Reading..."
    output=sys.argv[1]
    i=2
    while i < num_files:
        input_files.append(sys.argv[i])
        i=i+1

#--------------Working on input files---------
    urlerrors = open("urlerror.txt","w") # record any errors on a text file
    for input_file in input_files:
        int_keys = set()
        for line in open(input_file):
            line=line.strip()
            was_url = False # don't want to look for bibtex key if it was a url container
            for urlcontainer in urlcontainers:
                if re.match(urlcontainer,line,re.I):
                    was_url = True # lock the current iteration out of checking for bibtex keys
                    url_in_container = re.search(r'[\{][\s]*([^\s\}]+)[\s]*[\}]*',line,re.I).group(1) # this ugly expression was determined through trial and error. If you can find a prettier way to do this, please do.
                    urltest = Request(url_in_container)
                    try:
                        response = urlopen(urltest)
                    except URLError, e:
                        urlerrors.write('From {}: \n'.format(input_file))
                        urlerrors.write('{}\n'.format(url_in_container))
                        if hasattr(e, 'reason'):
                            urlerrors.write('Failed to reach server. Reason: {}\n'.format(e.reason))
                        elif hasattr(e, 'code'):
                            urlerrors.write('Server couldn\'t fulfil request. Error code: {}\n'.format(e.code))
                        else:
                            urlerrors.write('URL seems to have passed.\n')

            if not(was_url):
                for entrytype in entrytypes:
                    if re.search(entrytype.lower(),line.lower(),re.I):
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
		
