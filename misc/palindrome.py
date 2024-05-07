# solution 1
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_1(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = "".join(char.lower() for char in s if char.isalnum())

    # Compare the string with its reverse
    return s == s[::-1]


# solution 2 -  2 pointers + custom alpha numeric check
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_palindrome_2(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not is_alpha_numeric(s[l]):
            l += 1

        while r > l and not is_alpha_numeric(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


def is_alpha_numeric(c):
    return (
        (ord("a") <= ord(c) <= ord("z"))
        or (ord("A") <= ord(c) <= ord("Z"))
        or (ord("0") <= ord(c) <= ord("9"))
    )


input_string = "A man, a plan, a canal: Panama"
print(is_palindrome_1(input_string))
print(is_palindrome_2(input_string))
