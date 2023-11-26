def find_largest(numbers):
    if not numbers:
        return None  # Return the none for an empty list

    largest = numbers[0]  # assume the first number is the largest
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest


# Example ussage
my_list = [12, 45, 47, 23, 9, 4, 6]
result = find_largest(my_list)
print("The largest number is:", result)
