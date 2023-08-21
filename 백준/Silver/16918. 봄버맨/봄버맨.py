from collections import deque


def bfs(q,arr):

    while q:
        x,y = q.popleft()
        arr[x][y]='.'
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = dx+x,dy+y
            if 0<=nx<R and 0<=ny<C and arr[nx][ny]=='O':
                arr[nx][ny]='.'
        


def solve(t):
    global q, arr
    if t == 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j]=='O':
                    q.append((i,j))

    elif t % 2 ==1:
        bfs(q,arr)
        for i in range(R):
            for j in range(C):
                if arr[i][j]=='O':
                    q.append((i,j))
    #폭탄이 설치되어 있지 않은 모든칸에 폭탄 설치
    else:
        arr =[['O']*C for _ in range(R)]




R,C,N = map(int,input().split())

arr=[list(input().rstrip()) for _ in range(R)]
q= deque()



for i in range(1,N+1):
    solve(i)

for i in arr:
    print(''.join(i))