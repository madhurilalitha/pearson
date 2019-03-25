#!/usr/bin/perl

# perl commands to check perl typos and defines variables scope
use strict;
use warnings;
 
my %count; # hash
# a scalar variable
# here shift takes the first element of perl scripts arguments
# die is to print the statement and quit the program
# using my is like a local scope and signals that it is not a global variable
my $file = shift or die "Usage: $0 FILE\n";
# "<" is for read file operation
# fh is a file handler. We are trying to open a file
# quit the program if this step is unsuccessful
open my $fh, '<', $file or die "Could not open '$file' $!";
while (my $line = <$fh>) {
	# removes the newline from the input record
  chomp $line;
  # splits on string character
  foreach my $str (split /\s+/, $line)
  	 # a hash map where each unique string are keys and values are counts of strings
     $count{$str}++;
}

# sorting the keys chronological order
foreach my $str (sort keys %count)
	# priting each string and its count in the given file document
  printf "%-31s %s\n", $str, $count{$str};


"""

1. Q: What is this script doing?
   A: This script essentially:
   			(i) reading a file
   			(ii) iterating through each line
   			(iii) splitting each line on strings
   			(iv) prints the overall counts of each string in the given file

2. Q: Comment each line describing its function.
   A: Commented.

3. Q: Which functional test cases would you design to test the script above?
   A: Will update.

4. Q: Implement 2 of the test case in 3) in Perl or scripting of your choice.
   A: Will implement in python

"""