# Project Euler Problem 9
# find the pythagorean triplet for which a + b + c = 1000

import math
from math import sqrt

#checks if a number is prime or not
def is_prime(num):
    return

#Main method
def main():
    a = 0
    b = 0
    c = 0
    m = 1
    n = 1

    for m in range (1, 500, 1):
        for n in range (m + 1, 500, 1):
            a = n * n - m * m
            b = 2 * n * m
            c = n * n + m * m

            if (a + b + c == 1000):
                print "a = ", a
                print "b = ", b
                print "c = ", c
                print "product = ", a * b * c
    




#Start at main function
if __name__ == '__main__':
	main()
        