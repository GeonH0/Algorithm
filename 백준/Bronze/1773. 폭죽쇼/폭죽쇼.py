n,c  =map(int,input().split())
k =[0]*(c+1)

for i in range(n):
    n = int(input())
    if n ==1:
        print(c)
        quit()
    for j in range(n,c+1,n):
        k[j]=1
print(sum(k))
