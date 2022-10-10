n = int(input())
s=[]
k = list(map(int,input().split()))
k.sort(reverse=True)
print(k[len(k)//2])