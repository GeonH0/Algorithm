n= int(input())
data = sorted(list(map(int,input().split())))

q,r = divmod(n,2)
print(data[q+r-1])
