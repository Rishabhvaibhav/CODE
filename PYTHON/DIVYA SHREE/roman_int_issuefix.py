import re

value = True
while (value):
  #same loop as the test case
    roman_key_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500
    }
    
    input_roman = input("Enter a Roman Number till  800: ").upper()
    
    # i use regex to recheck the input
    # circumflex (^) and dollar sign ($) ker
    if not re.match(r'(CD|D?C{0,3})^(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', input_roman):#it will no longer strictly implement the pattern to match the entire string.
        print("Invalid Roman Number")
    else:

        result = 0
        prev_value = 0
        for i in reversed(input_roman):
            value = roman_key_value[i]
            if value >= prev_value:
                result += value
            else:
                result -= value
            prev_value = value
        print("The Value of the Entered Roman Number is:", result)

    