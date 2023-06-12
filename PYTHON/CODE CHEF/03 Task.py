while True:
    try:
        num1 = int(input("Input a 1st number: "))
        num2 = int(input("Input a 2nd number: "))
        if num1 % num2 == 0:
            print("A number is completely divisible by another number ")
        else:
            print("A number is not completely divisible by another nuumber ")
        break
    except ValueError:
        print("INVALID ")