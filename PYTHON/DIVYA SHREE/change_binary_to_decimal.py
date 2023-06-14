binary_input = input("Enter the Four digit binary number  ")
binary_numbers = binary_input.split(',')
binary_number = binary_input[::-1]


decimal = 0
valid_input = True
divi_5 = []

for i in range(len(binary_number)):
    decimal += int(binary_number[i]) * 2**i
    
print("The decimal number is:", decimal)

for number in binary_numbers:
    if len(number) != 4 or number == '0' and number == '1':
        valid_input = False
        break

    decimal = int(decimal)
    if decimal % 5 == 0:
        divi_5.append(decimal)
        
if valid_input and divi_5:
    # result_sequence = ','.join(divi_5)
    print("Numbers divisible by 5:")
elif valid_input:
    print("There are no number id divisible by 5 in this sequence")
else:
    print("Invalid Input ")

