#!/usr/bin/env python
def print_stuff():
    s1 = "Hello "
    s2 = "World\n"
    s3 = """ 
what in 
the world is happening with \
"""
    s3 += ' - hello world above? '

    s4 = ('\nnothing '
         'is wrong with it.')

    print (2 * (s1 + s2))  # multiplying string by 2 & using '+' on strings to concatenate
    print (s3)
    print (s4)
    print (s4[1:9] + s4[-17:-9])  # indexing the string characters, +ve and -ve indices
    print (s4[:-18])  # slicing of the string characters, (i.e. without specifying the start or end after ':')


# function list
print_stuff()
