fibonacci_sequence = [0, 1]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

first = 0
second = 1

for i in range(1, 101): # includes 0 but not 101 (repeats 100 times)

    next = first + second
    # we need to change first and second
    # the first number in the next iteration is the old second number
    old_first = first # store the old first
    first = second # first is old second
    second = old_first + second # second is old first + old second

    fibonacci_sequence.append(next)

print(fibonacci_sequence)








