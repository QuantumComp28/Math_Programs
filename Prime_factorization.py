#!usr/bin/python3.14

import numpy as np
import sys
    
def prime_factorization(num):

    factors=[]
    
   # Dealing with the 2 prime factors of
   # the given number.
   
    while num % 2 == 0:
       factors.append(2),
       num = num // 2
       
   # This makes our number odd so we can go from 3
   # And check each number with the divison trial
   # algorithm.

    for i in range(3,int(np.sqrt(num))+1,2):
                  while num % i == 0:
                      factors.append(i)
                      num = num // i
    if num > 2:
       factors.append(num)

    return print(factors)

while True:

    try:
        num=int(input(f'Please plug in an integer: '))
        prime_factorization(num)

    except (ValueError,AttributeError):
        print()
        print('The given value is not an integer',
            'Please try again.')
        print()

    while True:

        restart = input('\nInput another integer? (y/n): ').strip().lower()
        print()

        if restart == 'n':
            sys.exit()
        else:
            break


    


    
