#Project Euler Problem 2
first, second = 1, 2
sum = 0
while (first <= 4000000):
    if (first % 2 == 0):
        sum += first
    temp = second
    second = first + second
    first = temp
print(sum)
