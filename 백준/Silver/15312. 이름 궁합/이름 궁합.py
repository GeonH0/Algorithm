
arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = str(input())
B = str(input())
ans = []
for i in range(len(A)):
    ans.append(arr[ord(A[i])- 65])
    ans.append(arr[ord(B[i])- 65])
tmp = []

while len(ans) != 2:
    for i in range(1,len(ans)):
        tmp.append((ans[i]+ans[i-1])%10)
    ans = tmp
    tmp =[]
print(f"{ans[0]}{ans[-1]}")
