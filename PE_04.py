#Project Euler Problem 4
MAX_NUM = 999
MIN_NUM = 100

def isPalindrome(num):
    '''determines whether or not a number is a palindrome'''
    return str(num) == str(num)[::-1]


def calculateLargestPalindrome(min, max):
    maxPal = 0
    # calc product of all combinations of 2 numbers here?
    for i in range (min, max, 1):
        for j in range (min, max, 1):
            if (i * j) > maxPal and isPalindrome(i * j):
                maxPal = i * j
    return maxPal


def main():
    # find the largest palindrome
    # from the product of two 3-digit numbers
    # x * y = abcba

    largestPal = calculateLargestPalindrome(MIN_NUM, MAX_NUM)
    print largestPal

   
        





#Start at main function
if __name__ == '__main__':
	main()