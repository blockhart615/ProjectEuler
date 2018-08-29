# Project Euler Problem 12
# The first triangluar number with over 500 divisors

import time
import math
from math import sqrt


def find_num_divisors(num):
    '''Finds the number of divisors that the given number has'''
    numDivisors = 0
    root = int(math.ceil(sqrt(num)))
    
    for i in range (1, root, 1):
        if num % i == 0:
            numDivisors += 2

    if root * root == num:
        numDivisors -= 1

    return numDivisors


def main():
    '''main function'''
    num = 1  # keeps track of the triangle numbers
    counter = 2  # counter used to make triangle numbers

    # loop until 
    while find_num_divisors(num) < 500:
        num += counter
        counter += 1

    # output results
    print "The answer is ", num


# Start at main function
if __name__ == '__main__':
	main()
