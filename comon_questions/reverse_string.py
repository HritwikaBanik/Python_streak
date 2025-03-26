def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
        print(result)# Add each character to the front of the result string
    return result

# Example
print(reverse_string("Hello"))  # Output: "olleH"