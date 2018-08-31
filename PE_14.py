# Project Euler Problem 14
# Longest Collatz sequence
# if n even - n/2
# if n odd  - 3n+1
# find the number under 1 million that has the longest chain.


def calculate_collatz_sequence(num):
    chain = [num]

    while (num > 1):
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        chain.append(num)

    return chain


def main():
    '''main function'''
    MAX = 1000000
    num_with_longest_chain = 0
    longest_chain_len = 0

    for i in range (1, MAX + 1, 1):
        chain = calculate_collatz_sequence(i)
        if len(chain) > longest_chain_len:
            num_with_longest_chain = i
            longest_chain_len = len(chain)

    print "The number with the longest chain was ", num_with_longest_chain
    print "With a length of ", longest_chain_len


# Start at main function
if __name__ == '__main__':
	main()
