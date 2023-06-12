# input_value = ["1", 2, 3, ["x", 2, 3], [1, 2, 3, [1, 2, 3]]]
# input_value = str(input_value)
# print("Old Input Value:", input_value)

# remove = "["
# remove1 = "]"
# input_value = input_value.replace(remove, "")
# input_value = input_value.replace(remove1, "")
# input_value_list = eval(input_value)
# input_value_list = list(input_value_list)  # Convert tuple to list
# print("New Value:", input_value_list)

input_value = ["1", 2, 3, ["x", 2, 3], [1, 2, 3, [1, 2, 3]]]
input_value_str = str(input_value)
input_value_str = input_value_str.replace("[", "").replace("]", "")
input_value_list = input_value_str.split(",  ")
print("New Value:", input_value_list)


