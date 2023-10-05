
import sys
input = sys.stdin.readline

N,Y = input().split()
arr=[]
for _ in range(int(N)):
    arr.append(input())
arr = list(set(arr))



if Y == 'Y':
    print(len(arr))
elif Y == 'F':
    print(len(arr)//2)
elif Y == 'O':
    print(len(arr)//3)

