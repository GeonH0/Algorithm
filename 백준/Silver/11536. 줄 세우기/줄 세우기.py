import sys
input = sys.stdin.readline

n = int(input())
arr =[]
cnt =0
for _ in range(n):
    arr.append(input())

if sorted(arr) == arr:
        print("INCREASING")
elif sorted(arr, reverse=True) == arr:
        print("DECREASING")
else:
        print("NEITHER")