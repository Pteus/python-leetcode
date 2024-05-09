s = "A man, a plan, a canal: Panama"


def isPalindrome(s: str) -> bool:
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


# time: O(n)
# space: O(1)

print(isPalindrome(s))
