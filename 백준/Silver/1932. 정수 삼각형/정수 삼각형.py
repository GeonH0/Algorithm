

N= int(input())
rect = []
for _ in range(N):
    rect.append(list(map(int,input().split())))


for i in range(1,N):
    for j in range(len(rect[i])):
        if j==0:
            rect[i][j] = rect[i][j] + rect[i-1][j]
        elif j == len(rect[i])-1:
            rect[i][j] = rect[i][j]+rect[i-1][j-1]
        else:
            rect[i][j]=max(rect[i-1][j-1],rect[i-1][j])+rect[i][j]
print(max(rect[N-1]))