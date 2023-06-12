def bubble_sort(number):
    n = len(number)

    # Traverse through all numberay elements
    for i in range(n - 1,0,-1):
        # Last i elements are already in place
        for j in range(i):
            # swap is numbr is greater than next number
            if number[j] > number[j + 1]:
                temp = number[j]
                number[j] = number[j + 1]
                number[j + 1] = temp
                

# Example usage:
number = [2, 64, 34, 128,  3,4, 25, 12, 22, 11, 90 , 1]
bubble_sort(number)
print("Sorted number is :", number)
