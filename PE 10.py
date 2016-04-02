#part2
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

#sums the list of primes
def sum_primes(start):
    nextPrime = get_primes(start)
    LIMIT = 2000000  #LIMIT is the number we are generating up to
    num, sum = 0, 0
    while num < LIMIT:
        num = next(nextPrime)
        if num < LIMIT:
            sum += num
    print("THE SUM IS: ", sum)
    


def main():
    #print("Which number would you like to start from?")
    #start = input()
    sum_primes(2)
    


#Start at main function
if __name__ == '__main__':
	main()
