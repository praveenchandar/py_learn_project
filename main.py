#!/usr/bin/env python
def strings():
    print ('strings():-')
    s1 = "\nHello "
    s2 = "World"
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


def lists():
    print ('lists():-')
    squares = [0]
    for i in range(1, 10):
        squares += [i ** 2]  # adding new list elements to expand the list
    for i in range(11, 15):
        squares.append(i ** 2)  # adding new list elements to expand the list
    print (squares)
    squares1 = squares[2:5]  # slicing returns another list
    print (squares1)

    # print ('length of list = ', len(list1))
    # for i in list1:
    # print ("list(%d)", list1[0])


def fibonacci(n):
    print ('fibonacci(', n, '):-', end='')
    i, a, b = 0, 0, 1  # multiple assignment
    while (i < n):
        print(a, end=',')
        i, a, b = (i + 1), b, a + b  # multiple assignments, right hand side of '=' is evaluated first (from left to right)


def user_prompt():
    print ('********************************************************************')
    # function list
    loop = True
    while loop:
        fn = ['exit', 'strings', 'lists', 'fibonacci']
        print(fn, end=',')
        user_input = input('\nChoose option:')
        print('-----------------------')
        valid = False
        for entry in fn:
            if user_input == 'exit':
                print('--- exit done ---\n')
                loop = False
                break
            elif user_input == entry:
                eval(entry + '()')
                print ('\n********************************************************************')


user_prompt()
