def Fibonacci(i):
    if i <= 1:
        return [0] * (i + 1)
    elif i == 2:
        return [0, 1]
    else:
        sequence = Fibonacci(i - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

num = int(input("Input: "))
print("Output:", Fibonacci(num))
