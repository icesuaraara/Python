def Cal1():
    Grade = 1
    while Grade != 0:
        Grade = int(input("Enter Grade :"))
        if Grade>=80:
                print("Your Grade A")
        elif Grade>=75:
            print("Your Grade B+")
        elif Grade >=70:
            print("Your Grade B")
        elif Grade >= 65:
            print("Your Grade C+")
        elif Grade >= 60:
            print("Your Grade C")
        elif Grade >= 55:
            print("Your Grade D+")
        elif Grade >= 50:
            print("Your Grade D")
        else:
            print("Your Grade F")
    print("\nEnd Program")

Cal1()