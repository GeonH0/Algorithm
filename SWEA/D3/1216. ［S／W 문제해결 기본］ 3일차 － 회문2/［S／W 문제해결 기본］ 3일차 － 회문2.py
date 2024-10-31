def is_palindrome(s):
    return s == s[::-1]
 
def solve(s):
    n = len(s)
    max_len = 0
     
    for i in range(n):
        for j in range(i+1, n+1):
            if is_palindrome(s[i:j]):
                max_len = max(max_len, j-i)
     
    return max_len if max_len > 0 else 0
 
s = input()
result = solve(s)
print(result)