

input_value = [1, 2, 3, [1, 2, 3], [1, 2, 3, [1, 2, 3]]]
flat_list = sum(input_value, [])
print(flat_list)


input_value = [1, 2, 3, [1, 2, 3], [1, 2, 3]]
flatten_list = []

for i in input_value:
    if type(i) == list:
        flatten_list.extend(i)
    else:
        flatten_list.append(i)
        
print(flatten_list)
        





















