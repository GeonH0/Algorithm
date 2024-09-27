def next_permutation(s):
    s = list(s)
    n = len(s)
    i = n - 1

    # 1. i 찾기
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1

    if i <= 0:
        return '없음'

    # 2. j 찾기
    j = n - 1
    while s[j] <= s[i - 1]:
        j -= 1

    # 3. 교환하기
    s[i - 1], s[j] = s[j], s[i - 1]

    # 4. 뒤집기
    s[i:] = s[i:][::-1]

    return ''.join(s)
    
N = int(input())
for _ in range(N):
    word = input().strip()
    if next_permutation(word) == "없음":
        print(word)
    else:
        print(next_permutation(word))