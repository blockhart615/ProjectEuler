from math import sqrt
import math

#Checks whether a number is prime
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

def main():
    largestPrime = 1
    num = 600851475143
    for i in range(3,math.ceil(sqrt(num)) + 1, 2):
        if (num % i == 0):
            if (is_prime(i)):
                largestPrime = i
    print(largestPrime)


#Start at main function
if __name__ == '__main__':
	main()
