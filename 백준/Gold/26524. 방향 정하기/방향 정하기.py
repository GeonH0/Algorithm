n = int(input())
p = 10**9 + 7
ans = 1
for i in range(1,n+1):
    ans = (ans*i) %p
print(ans)