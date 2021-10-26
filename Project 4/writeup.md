Alt - Project 4
===============
## Team Members:

- Hunter Harris
- Jeffery Ho

## Expected Data Structures

	As a group we think that an ArrayList, whether it be similar to python's built 
in list or closer to the Array List class that we wrote would be a good choice as far
as data structures go for use in coverage. Each line could be represented as an index,
maybe even each line number as the index, with a boolean value used to state whether
the line has been checked or not. Another idea is to have a sort of list as the value
in our giant array list. Inside these individual lists could be things like the 
aforementioned boolean values, as well as possibilities like having a string of the
actual code or maybe an incremented of how many times the line has been called.

## Initial Code Examination

	At first glance the source tree is packed with, folders to other files, documents 
of type .ini and .txt along with python files and unix executables. The source file is 
located in a folder titled "Coverage" and is made up almost entirely of python files with 
a few .html and .c++ files. Most of the python files range in size from 10 lines - 1,200 
lines. The C++ files are interesting because they're used to rewrite part of the core 
python code.

	One thing we noticed while looking at the files is that the ratio of test files to
source files is almost 1 to 1. These testing files, similar to the python source files,
have a fairly large size range from less than 10 lines to over 1,000 on the larger ones.

The files we chose were:

	test_coverage.py: The file name was true to its purpose which was chiefly to ensure 
		the accuracy of coverage function.

	test_debug.py: This file appeared to test "formats" and "debug_output", both of which 
		we assume are functions.

	cmdline.py: This file's use seemed to be calling coverage as a whole from the command
		line.

	config.py: Config's job was hard to place exactly but it should be noted that this
		file appeared to take a lot of inputs and "configure" them to the attributes of 
		the coverage file.

	control.py: This file is the core control for coverage.py. It seems like this is the
		file that coverage runs out of.

	data.py: This is the file that collects all the data calculated such as missed lines
		and coverage percentage.

	debug.py: Debug appears to be used as a tool to help the user debug their file.

Which is more valuable, code or comments?
	Our group came to the conclusion that while reading the code, the comments prove
to be more useful in gaining insight into the purpose of the file/function.

## Detailed Code Examination

	File: data.py
	
	Before looking at this files specific code but after knowing its general purpose, our
group thought that our array list data structure would be the best data structure for holding
the values and information tasked to this file. The file's main class, CoverageData, is best 
described as a collection of dictionaries used to store data such as line numbers, module 
names, and information about the program execution. CoverageData is first initialized by using
data from multiple other source files and combining this information into one class. Creating
this behemoth of a class is done through a series of functions including the two listed below.

	"arcs(filename)" - will find lines that have been checked and return a list of tuples
		representing lines that have been run. ex: [(10, 17), (21, 35)]
	"add_arcs(arcdata)" - this function will take the list returned by the previous function
		and record the lines that have been run into the dictionary.
	
	CoverageData's sole purpose appears to be the collection and storage of data in one,
central location. We can assume that data.py is then referenced profusely throughout the rest
of Coverage because all the information needed for calculations and printing to screen is
located in the CoverageData class.

## Summary

	As a whole the source code for Coverage is pretty easily readable thanks to the comments
written to indicate each function's purpose. The comments are used to give a general overview
of the though process and utility of the code being written which makes reading, editing,
and debugging the code much much easier. As a group we decided that we are confident that
maintain and updating this code would be feasible... for the right price. 