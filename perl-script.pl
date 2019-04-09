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
   			in a sorted way.

2. Q: Comment each line describing its function.
   A: Commented.

3. Q: Which functional test cases would you design to test the script above?
   A: 1) File does not exist and validate whether an exception is raised
      2) File exists but the text in the file is empty
      3) File exists and the text has equal number of words (all counts are
      equal)
      4) File exists and the text has digits as well apart from string words


4. Q: Implement 2 of the test case in 3) in Perl or scripting of your choice.
   A: Please find the below test cases

"""


import unittest

class TestFileWordCounts(self):
    """let us say the above perl function is wrapped in a python function"""
     """called get_word_counts"""

    def test_01_file_does_not_exist(self):
        test_data = "random_file.txt"
        with self.assertRaises(FileNotFoundError) as exe:
            sorted_word_counts = get_word_counts("some_missing_file_name")
        actual_exception = str(exe.exception)
        assert "Could not open" in actual_exception

    def test_02_file_exists_but_file_is_empty(self):
        """as the file is empty the sorted word counts dict will be empty"""
        test_data = "some_existing_file.txt"
        sorted_word_counts_dict = get_word_counts("some_missing_file_name")
        assert {} is sorted_word_counts_dict
        
        
