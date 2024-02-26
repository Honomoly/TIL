def check_palindrome(text):
    N = len(text)
    N_half = int(N/2)
    result = True
    for i in range(N_half):
        if text[i] != text[N-i-1]:
            result = False
            break
    return result