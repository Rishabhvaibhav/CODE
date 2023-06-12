
# def anagram():
#     str1 = input("Enter the first String:")
#     str2 = input("Enter the second String:")
    
#     if sorted(str1) == sorted(str2):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")
#     return anagram()
    
# print(anagram())




def anagram():
    str1 = input("Enter the first String:")
    str2 = input("Enter the second String:")
    
    if len(str1) != len(str2):
        print("The strings aren't anagrams.")
        return
    
    str1_chars = list(str1)
    
    for char in str2:
        if char in str1_chars:
            str1_chars.remove(char)
        else:
            print("The strings aren't anagrams.")
            return
    
    if len(str1_chars) == 0:
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
    
anagram()
