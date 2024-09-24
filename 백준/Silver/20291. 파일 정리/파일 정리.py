
N = int(input())
ans = {}
for _ in range(N):
    file = input()
    a,b = file.split('.')
    if b in ans:
        ans[b] +=1
    else:
        ans[b] = 1

for key in sorted(ans):
    print(f"{key} {ans[key]}")