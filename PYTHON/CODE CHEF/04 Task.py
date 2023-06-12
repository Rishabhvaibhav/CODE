#Program that accepts an integer (n) and computes the value of (n+nn+nnn)

while True:
    try:
        n = input("Enter the number:  ")
        n = int(n)
        case2 = str(n) + str(n)
        case3 = str(n) + str(n) + str(n)
        compute = n + int(case2) + int(case3)
        print('n + nn + nnn = ',n,'+',n,n,'+',n,n,n , '=' , compute)
        break
    except:
        print("Invalid , Your input is not integer")

             
        