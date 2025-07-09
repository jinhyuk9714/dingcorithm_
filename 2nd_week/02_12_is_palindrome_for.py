str = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if str[i] != str[n - 1 - i]:
            return False
    return True


print(is_palindrome(str))
