n = int(input())
price = list(map(int,input().split()))
cnt = 0
price.sort()

cnt = sum(price[(n+1)//2:])*2
if n%2==1:
    cnt+=price[n//2]
print(cnt)
