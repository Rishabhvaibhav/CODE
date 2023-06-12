
def find():
    input_list = input("Enter the numbers:").split(',')
    
    maxi = input_list[0]
    mini = input_list[0]
    for i in input_list:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
    print("The maximum number is:", maxi)
    print("The minimum number is:", mini)

find()
