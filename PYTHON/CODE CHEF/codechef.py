t = int(input("Enter the Number of test case You want to perform"))
for i in range(t):
    expense, income = map(int, input("Enter the Expense and Income ").split())
    
    
    
    
    
    
    
    
    
    income = 2**income
    expense = income // 2
    saving = income - expense
    debt = expense - income
    
    
    if expense > income:
        print(debt)
    elif expense == income:
        print("Balance")
    elif expense < income:
        print(saving)
    else:
        print("Invalid Input")

