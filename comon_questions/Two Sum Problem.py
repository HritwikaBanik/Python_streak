#Input: [2, 7, 11, 15], target = 9
#Output: [0, 1] (because 2 + 7 = 9)


def two_sum(arr: list, target: int):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):  # Check every pair of numbers after the current element
            if arr[i] + arr[j] == target:
                return [i, j]  # If a pair is found, return their indices

# Example usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
