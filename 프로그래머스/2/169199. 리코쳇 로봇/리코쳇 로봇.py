from collections import deque

def solution(board):
    def bfs(si, sj):
        q = deque()
        q.append((si, sj))
        v = [[0] * C for _ in range(R)]
        v[si][sj] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            ci,cj = q.popleft()
            if board[ci][cj] == 'G':
                return v[ci][cj]

            for i in range(4):
                ni,nj = ci,cj
                while True:
                    ni += dx[i]
                    nj += dy[i]
                    if (ni < 0 or ni >= R or nj < 0 or nj >= C) or board[ni][nj]=='D':
                        ni -= dx[i]
                        nj -= dy[i]
                        break

                if v[ni][nj] == 0:
                    v[ni][nj] = v[ci][cj] +1
                    q.append((ni,nj))

    R = len(board)
    C = len(board[0])
    ans = float('inf')
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'R':
                result = bfs(i,j)
                if result is not None and result < ans:
                    ans = result
                    
    answer = ans -1 if ans != float('inf') else -1
    return answer
