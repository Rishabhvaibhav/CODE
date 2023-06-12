# a =[1,2,3,4,5,6,7,8]
# value = 0
# for i in a:
#     if i % 2 == 0:
#         pass
#         # value =  i
#     value += 1
# print("{  Even  : ",value , "}")



# Name = "RishAbhVaibhav"
# reversed = ''

# for i in Name:
#     reversed = i + reversed
# print("CASE 1 : ",reversed)

# for c in Name:
#     reverse = Name[::-1]
# print("CASE 2 : " , reverse)


# intro = "My Name is Rishabh Vaibhav"

# rev = ''      

# for i in range (len(intro)-1,-1,-1):
#     rev = rev + intro[i]
# print(rev)

#This for loop is used to iterate over the indices 
#of intro in reverse order. It starts from len(intro)-1 
#(the last index of intro) and decrements by 1 until it 
#reaches -1. The range function is used here to generate a 
#sequence of indices to iterate over.

# myintro = "Rishabh Vaibhav"
# revs = ""

# for i in myintro:
#     revs = i + revs

# print(revs)



# number = 0
# while (number < 5):
#     number = number + 1
#     print("number is : ",number)


# str1 = "hello"
# print('h' in str1)
# print('rv' in str1)


# list1 = [1,2,3,4564,53698,6555,755,878,999]
# print(999 not in list1)
# print(999  in list1)
# print(50 not in list1)



# for i in range(10,1,-1):
#     print(i)

# roman_values = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }

# roman_numeral = input("Enter a Roman numeral: ")
# total = 0
# i = 0

# while i < len(roman_numeral):
#     current_value = roman_values[roman_numeral[i]]

#     if i + 1 < len(roman_numeral):
#         next_value = roman_values[roman_numeral[i + 1]]

#         if current_value < next_value:
#             total += next_value - current_value
#             i += 2
#         else:
#             total += current_value
#             i += 1
#     else:
#         total += current_value
#         i += 1

# print("Numerical value:", total)


roman = {"I":1,
         "V":5,
         "X":10}
input= input("Enter a roman number : ")
total = 0
i = 0
while i < len(roman):
    current_value = roman[input[i]]
    if i + 1 < len(roman):
        next_value = roman[input[i+1]]
        if current_value < next_value:
            total += next_value - current_value
            i += 2
        else:
            total += current_value
            i += 1
    else:
        total += current_value
        i += 1




















# z = input("Enter a roman number : ")
# for i in roman:
#     if i == "I":
#         print(roman[i])
#     elif i == "X":
#         print(roman[i])
#     elif i == "V":
#         print(roman[i])

        
        
