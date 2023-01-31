n = int(input())
arr=list(map(int,input().split()))

num  = set(arr)
a = list(num)
a.sort()

b = {a[i]:i for i in range(len(a))}
for i in arr:
    print(b[i],end =' ')