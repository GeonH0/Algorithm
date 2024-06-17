
N = int(input())
arrA = []
arrB = []
arrC = [[0]*N for _ in range(N)]
cnt = 0
for _ in range(N):
    arrA.append(list(map(int,input().split())))
for _ in range(N):
    arrB.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arrA[i][k] & arrB[k][j]:
                cnt +=1
                break

print(cnt)


