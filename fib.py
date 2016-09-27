#!/usr/bin/env python
"""
This program takes a command line argument n (positive integer) and prints the nth fibonacci number.
"""

#
### INSTRUCTOR COMMENT:
# See the sequences file for my main comments, which are repeated here.
# Also, imports should be done at the top of the file, ideally, except for
# specific imports needed only for the __main__ block, which should be at the
# top of the __main__ block.
#

def main(argv):
    """
    This function will execute if fib.py is run from the command line. It prints the nth fibonacci number.
    """
    #importing sequences.py as a module
    import sequences as seq
    #ensuring that there are enough command line arguments
    if len(argv)<2:
        print "Not enough command line arguments."
        from sys import exit
        exit(1)
    #printing the nth fibonacci number
    print seq.fibonacci(int(argv[1]))[-1]

def test_main():
    """
    Tests the functioning of main(argv) by executing the program and checking the output string.
    """
    from subprocess import get_output
    assert check_output(['./fib.py','10'],'r') == '55'

if __name__ == "__main__":
    from sys import argv
    main(argv)
