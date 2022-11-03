n= int(input())
def mi(a,b):
    for j in range(min(a,b),0,-1):
        if a%j==0 and b%j==0:
            print(j)
            break
def ma(a,b):
    for j in range(max(a,b),(a*b)+1):
        if j%a==0 and j%b==0:
            print(j)
            break



for i in range(n):
    a,b= map(int,input().split())
    ma(a,b),mi(a,b)
    