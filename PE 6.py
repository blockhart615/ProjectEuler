#Project Euler Problem 6
def sumOfSquares(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + (i**2)
    return sum

def squareOfSums(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum**2


def main():
    num = 100
    s1 = sumOfSquares(num)
    s2 = squareOfSums(num)
    print("Sum of Squares: ", s1)
    print("Square of Sums: ", s2)
    difference = squareOfSums(num) - sumOfSquares(num)
    print("difference: ", difference)


#Start at main function
if __name__ == '__main__':
	main()
        
