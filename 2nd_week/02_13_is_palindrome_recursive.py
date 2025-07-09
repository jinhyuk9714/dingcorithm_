text = "abcba"


def is_palindrome(text):
    if text[0] != text[-1]:
        return False
    if len(text) <= 1:
        return True
    return is_palindrome(text[1:-1]) # abcba -> bcb -> c


print(is_palindrome(text))
