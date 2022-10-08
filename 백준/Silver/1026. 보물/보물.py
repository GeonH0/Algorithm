

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

s_a = sorted(a,reverse=True)
s_b = sorted(b)

s = 0

for i in range(n):
    s += s_a[i]*s_b[i]

print(s)