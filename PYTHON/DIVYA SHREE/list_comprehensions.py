# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)
# print(ls)


# ls=[i for i in range(100) if i%3 == 0 ]
# print(ls)

dict = {z:f"item {z}" for z in range(1,10) }  #the f is used to create formatted string literals, also known as f-strings.
print(dict)

# dict1 = {value:key for key,value in dict.items()}
# print(dict1)

dress = {dress for dress in ["dress1","dress2","dress3","dress2","dress1","dress2"]}
print(dress)
print(type(dress))


# list1 = input["how many List u want to make "]

# list2 = input()

# list3 = [i for i in list2]
# print(list3)

"""The task is i want to take the list input from the user and then i want to ask the user how many list he want to make and then i want to make the list of list
then i ask which list he want to print like dict , list, set and then print the list as he want to print
"""
