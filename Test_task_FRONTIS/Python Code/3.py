def Pattern(n):
    for i in range(n):
        line = ''
        for j in range(n):
            if i == j or i + j == n - 1:
                line += '*'
            else:
                line += '-'
        print(line)

num = int(input("Input: "))
Pattern(num)

