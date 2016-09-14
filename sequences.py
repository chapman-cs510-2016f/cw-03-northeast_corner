#!/usr/bin/env python
import sys as sys
"""
This program contains a function fibonacci(n) that generates lists of fibonacci numbers.
Three test functions are included for fibonacci()
A main(argv) function is included to run from the command line.
"""

def fibonacci(n):
    """
    This function takes a positive integer argument and returns a list containing
    the Fibonacci numbers up to the nth.
    """
    #Checking for incorrect inputs and aborting if n isnt a positive integer
    if (n<=0) or (n%1!=0):
        print 'Improper input: must be a positive integer'
        sys.exit(1)
    #Initializing the list with the first element fib[0]=1 (ie. @ n=1, F(1)=1)
    fib = [1]
    for i in range(n-1):
        #Ensuring that fib[1]=1
        if i==0:
            fib.append(1)
        else:
            fib.append(fib[-1]+fib[-2])
    return fib

def test_fibonacci1():
    """
    This function ensures that fibonacci(1000) gives the correct output by direct comparison with known value.
    The L indicates that this is a 'long integer' which is essentially just an integer longer than the standard
    integer length (in terms of bytes in memory).
    """
    #Unfortunately, this requires actually inputting a long integer
    assert fibonacci(1000)[-1] == \
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L

def test_fibonacci2():
    """
    This function tests fibonnaci() by comparing the first ten to known values
    """
    fibNumbers = fibonacci(10)
    assert fibNumbers == [1,1,2,3,5,8,13,21,34,55]

def test_fibonacci3():
    """
    This function tests fibonnaci() by checking that elements are equal to the sum of the two previous elements
    """
    fibNumbers = fibonacci(10)
    for i in range(2,10): #skipping the first two
        assert fibNumbers[i] == fibNumbers[i-1] + fibNumbers[i-2]

def main(argv):
    """
    This function will execute if sequences.py is run from the command line. It prints the fibonacci sequence
    up to n where n is a command line argument.
    """
    if len(argv)<2:
        print "Not enough command line arguments."
        from sys import exit
        exit(1)
    print fibonacci(int(argv[1]))

def test_main():
    """
    Tests the functioning of main(argv) by executing the program and checking the output string
    """
    from subprocess import get_output
    assert check_output(['./sequences.py','10'],'r') == '[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]'

if __name__ == "__main__":
    from sys import argv
    main(argv)
