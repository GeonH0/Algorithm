import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr1 =set()
cnt =0

for _ in range(n):
    arr1.add(input())

for i in range(m):
    s = str(input())
    if s in arr1:
        cnt +=1
        



print(cnt)

            

    
            
