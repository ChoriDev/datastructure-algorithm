def get_fibonacci_numbers(n):
    bottom_up_table = []
    bottom_up_table.append(0)
    bottom_up_table.append(1)

    for i in range(2, n + 1):
        bottom_up_table.append(bottom_up_table[i - 1] + bottom_up_table[i - 2])
    
    return bottom_up_table

fibonacci_numbers = get_fibonacci_numbers(40)

T = int(input())

for i in range(T):
    N = int(input())

    if N == 0:
        print(1, 0)
    else:
        print(fibonacci_numbers[N - 1], fibonacci_numbers[N])