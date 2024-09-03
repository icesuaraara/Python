def AB(a, b):
    if a < b:
        return AB(b, a).replace('A', 'X').replace('B', 'A').replace('X', 'B')
    
    result = []
    while a > 0 or b > 0:
        if a > 0:
            result.append('A')
            a -= 1
        if a > b:
            result.append('A')
            a -= 1
        if b > 0:
            result.append('B')
            b -= 1
        if len(result) >= 3 and result[-3:] == ['A', 'A', 'A']:
            return "error"
    return ''.join(result)

a = int(input("Input number of A: "))
b = int(input("Input number of B: "))

print("output:", AB(a, b))
