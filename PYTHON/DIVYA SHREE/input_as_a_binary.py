binary_input = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
binary_numbers = binary_input.split(',')

valid_input = True
divi_5 = [] # means divisible by 5

for number in binary_numbers:
    if len(number) != 4 or number == '0' and number == '1':
        valid_input = False
        break

    decimal_number = int(number)
    if decimal_number % 5 == 0:
        divi_5.append(number)

if valid_input and divi_5:
    result_sequence = ','.join(divi_5)
    print("Numbers divisible by 5:", result_sequence)
elif valid_input:
    print("No numbers are divisible by 5.")
else:
    print("Invalid input. Please enter a sequence of comma-separated 4-digit binary numbers.")
