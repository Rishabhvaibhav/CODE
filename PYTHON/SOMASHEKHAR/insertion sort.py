def insertion_sort(number):
    n = len(number)

    # Traverse through 1 to n-1
    for i in range(n):
        minpos = i
        for j in range(i + 1, n):
            if number[minpos] > number[j]:
                minpos = j
                
        # Swap the found minimum element with the first element
        temp = number[i]
        number[i] = number[minpos]
        number[minpos] = temp
    

# Example usage:
number = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(number)
print("Sorted number is  :", number)
