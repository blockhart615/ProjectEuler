def infiniteGenerator():
    num = 20
    while True:
        yield num
        num += 20

def main():
    smallestFound = False
    numGenerator = infiniteGenerator();
    while (not smallestFound):
        num = next(numGenerator)
        if (num % 20 == 0):
            if (num % 19 == 0):
                if (num % 18 == 0):
                    if (num % 17 == 0):
                        if (num % 16 == 0):
                            if (num % 15 == 0):
                                if (num % 14 == 0):
                                    if (num % 13 == 0):
                                        if (num % 12 == 0):
                                            if (num % 11 == 0):
                                                smallestFound = True
    print(num)
        





#Start at main function
if __name__ == '__main__':
	main()
