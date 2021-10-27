# Lab 1

## 1 - Git
Well, folks, we’re going to be using git this quarter.

I’m not going to try to include a full intro to Git here; instead, I’m just going to tell you what you need to do for the lab:

1. Sign up for a GitHub account, if you don’t already have one.
2. Click on the invitation link to create your own private repository for this assignment.
3. Check out your fresh new repo. It should contain a file named *"lab1.py"*.
4. Edit this file to add a comment to Section 1, part 1, containing the word "persnickety".
5. Stage, commit, and push your change.
6. Log into github using their web interface; make sure you can see your Lab 1 repo, and the word "persnickety."

The rest of this lab contains many sections and many numbered parts of each section. You’ll see that the *"lab1.py"* template comes with lines indicating each of these sections and parts. You should put your answers to each part in the corresponding place in the code. Your code will be sliced and diced programmatically, so if you put your work in the wrong part of the file, or delete or alter the existing headers, you might not get credit for your work, and that would make us both sad.

## 2 - Data Definitions
  Each of the following programs requires a data definition. In many cases, it may be just a single commented line. In other cases, the data definition may require creation of a new class. In this case, be sure to    include all of the methods required by a new class: __init__, __repr__, and __eq__.

Provide two examples for each data definition.
1. A program that converts celsius to fahrenheit temperatures must accept a celsius temperature as input, and return a fahrenheit temperature as a result. Write a data definition for each of these two kinds of values.
2. A store might maintain a database that includes prices for various items. Write a data definition for a price (just the price), in cents.
3. Following on the prior item, write a data definition for a price record; it should include both the item’s name and its price.
4. A web browser might maintain information about open tabs. Develop a data definition for an open tab, that includes the URL being visited and the most recent date on which it was loaded. (Yes, this data definition may require sub-data-definitions).

## 3 - Signature, Purpose Statements, Headers
For each of the following functions, provide a signature, a purpose statement, and a header. You do not need to provide the data definitions; you may assume that this has already been done. Many of these problems are underspecified; make reasonable assumptions.
1. A function that accepts a price and adds sales tax,
2. a function that finds the price for a named item in a store’s price database,
3. a function that computes the median income using a given geographic region and given database, and
4. a function that accepts a given geographic region and database and determines which cities overlap with that region.

## 4 - Test Cases
For each of the following, write a contract, a purpose statement, a header, and a set of test cases. Each test case should take the form of a method whose name begins with *test*, containing a sequence of calls to *self.assertEqual*.

1. None of these require a separate data definition.
2. A function that accepts three distinct numbers and returns the second largest,
3. a function that accepts a string and returns true if it has no capital letters,
4. a function that accepts the names of two states and returns the "northernmost" one; that is, the one that contains the point closest to the north pole.

## 5 - Whole Functions
Follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design the following functions.

Place all of your tests for this section in a single *TestCase* class, so that you can run them. (This will also be helpful for automatic grading.)

Apologies to those of you that experience flashbacks during the following problems.
1. Develop the *f2m* function, that accepts a length represented as a number of feet and returns the corresponding length in meters.
2. Develop a data definition for a Musical Note, which includes a pitch represented as a frequency in Hz, and a duration represented as a length in seconds.
3. Develop the *up_one_octave* function, that accepts a note and returns a new note that is higher by one octave. In other words, its frequency is doubled.
4. develop the *up_one_octave_m* function, that accepts a note and mutates it to double its frequency, returning None. Be sure to test both the mutation and the return value.