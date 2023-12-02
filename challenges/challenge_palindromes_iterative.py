def is_palindrome_iterative(word):
    if not word:
        return False

    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False

    return True
