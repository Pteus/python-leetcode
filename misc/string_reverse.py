# solution 1
# O(n)
#   Slicing ([::-1]) creates a new string with the reverse of the original string. This operation involves copying each character of the original string to the new string, which takes O(n) time, where n is the length of the input string.
# O(n)
#   Since we are creating a new string to store the reversed string, the space complexity for this operation is O(n), where n is the length of the input string.
def reverse_string_1(s):
    return s[::-1]


# solution 2
# O(n)
#   Iterating through each character of the input string takes O(n) time, where n is the length of the input string.
#   Prepending each character to the reversed_str variable takes O(1) time.
# O(n)
#   The space complexity is determined by the additional space used for storing the reversed string (reversed_str). Since we are creating a new string, the space complexity for this operation is O(n), where n is the length of the input string.
def reverse_string_2(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_string = "Hello, world!"
print(reverse_string_1(input_string))
print(reverse_string_2(input_string))
