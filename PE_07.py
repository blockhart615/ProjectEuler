#Project Euler Problem 7

import math
from math import sqrt

#checks if a number is prime or not
def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3,math.ceil(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False  
        return True

#Generator that gets prime numbers
def get_primes(num):
    while True:
        if is_prime(num):
            yield num
        num += 1

#Main method
def main():
    num = 1
    getPrime = get_primes(num)
    nthPrime = 0
    while (nthPrime <= 10001):
        num = next(getPrime)
        nthPrime += 1
    print(num)


#Start at main function
if __name__ == '__main__':
	main()
        
