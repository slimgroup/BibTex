#!/usr/bin/perl

$BIBFILE = "slimbib.bib";
$BIBOUTFILE = ">slimbib_local.bib";
open (BIBFILE) or die("Could not open bib file.");
open (BIBOUTFILE) or die("Could not open bib output file.");
$pattern1 = 'Talkurl';
$pattern2 = 'talkurl';
$pattern3 = '\s+pdf';

foreach $line (<BIBFILE>) {
    if ($line =~ m/$pattern1/) {
       my $i = rindex($line, "/");
       $filename = substr($line, $i + 1);
       print BIBOUTFILE "\tTalkurl = {Slides/" . $filename;
    }
    elsif ($line =~ m/$pattern2/) {
       my $i = rindex($line, "/");
       $filename = substr($line, $i + 1);
       print BIBOUTFILE "\ttalkurl = {Slides/" . $filename;
    }
    elsif ($line =~ m/$pattern3/) {
       my $i = rindex($line, "/");
       $filename = substr($line, $i + 1);
       print BIBOUTFILE "\tpdf = {PDF_Papers/" . $filename;
    }
    else {
       print BIBOUTFILE $line;
    }
}
    
    
   
