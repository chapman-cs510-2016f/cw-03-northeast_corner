# CS510 CW 3

**Author(s):** Eric Freda and Kaiqin Huang

[![Build Status](https://travis-ci.org/chapman-cs510-2016f/cw-03-northeast_corner.svg?branch=master)](https://travis-ci.org/chapman-cs510-2016f/cw-03-northeast_corner)

**Due date:** 2016/09/20

## Specification

Complete the following exercises, saving your solutions in the indicated files. For Python files that include test functions, GitHub will automatically run your tests with ```nosetests``` on every commit, indicating any failures via the Travis framework in the build status image above.

1. Create a python file ```sequences.py``` with a function ```fibonacci(n)``` that returns the first ```n``` Fibonacci numbers in a list. (Recall that each successive Fibonacci number is defined by summing the previous two, starting with the numbers 1 and 1.) Commit to GitHub.
    * Hint: Use the python template file in the info repository to make sure you have the correct structure. You should have a #! line at the top, a module docstring, function definitions, function docstrings, and informative comments in your code.
    * Example: ```fibonacci(5)``` should return ```[1,1,2,3,5]``` 
    * Example: the last element of ```fibonacci(1000)``` should be: 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L (Note: what does the L at the end of this integer mean in Python? Explain in your module docstring.)
    * Write 3 test functions that verify whether this function outputs the correct results.  
    * Make sure the function only returns a list. Have it throw an exception if a nonsensical argument ```n``` is given (i.e., not a positive integer).
1. Write an executable python script ```fib.py``` that loads ```sequences.py``` as a module, reads one command line argument ```n```, runs ```fibonacci(n)```, then prints the last element of the result. Commit the script to GitHub.
    * If an exception is thrown, catch it and print an appropriate error message to the screen. 
    * Make sure you use the template to set up a proper ```main(argv)``` method called from inside a ```___main___``` environment. Your script should not execute any code if it is loaded as a module.
    * Remember to make your script executable with ```chmod```. 
    * Write a test function to verify that the main function operates as intended. 
1. Write a bash script ```runfibs.sh``` that uses bash to run ```fib.py``` for arguments ```n``` from 1 to 10000.  For each argument, redirect the output of the script to a comma-separated-value file ```fibs.csv``` such that each fibonacci number is separated by a comma (with no newlines). Commit the shell script (but not the csv file) to GitHub.
    * If a ```fibs.csv``` file already exists, back it up: move the existing file to ```fibs.csv.bak```, then create the new file. Inform the user that this backup occurred.
    * If a backup already exists, inform the user, then exit the program with an error code (not 0) before any files are overwritten.


## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

Outputting to a csv file required figuring out a way to get the formatting right, which will be useful if that needs to be done again. The bash script for n from 1 to 10000 might be a bit excessive--the sage cloud servers didn't seem to enjoy that so 100 was used instead. As it turns out, generating lists with an average size of 5000 elements that happen to contain extraordinarily large integers 10000 times takes a while.

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Eric Freda and Kaiqin Huang
