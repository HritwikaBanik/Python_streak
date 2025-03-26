def largest_element(arr: list):
    largest = arr[0]  # Initialize with the first element.
    for i in range(1, len(arr)):  # Start from the second element.
        if arr[i] > largest:
            largest = arr[i]  # Update largest if a larger element is found.
    return largest  # Return the largest element.

print(largest_element([2, 5, 3, 1, 4, 25, 2]))
