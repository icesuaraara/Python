
def cal_mul():
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    for i in range(number2+1):
        print(f"{i}. {number1} x {i} = {number1*i} ")
    
cal_mul()