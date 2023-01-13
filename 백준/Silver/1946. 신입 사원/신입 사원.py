import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    r= [list(map(int,input().split())) for _ in range(n)]
    r_a = sorted(r)
    top = 0
    answer = 1

    for i in range(1,len(r_a)):
        if r_a[i][1] < r_a[top][1]:
            top = i
            answer+=1

    print(answer)