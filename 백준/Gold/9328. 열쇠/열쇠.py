from collections import deque
import sys

def bfs():
    global keys
    q = deque()
    
    # 방문해야 할 문을 저장하는 딕셔너리 (A~Z)
    doors = {chr(i): [] for i in range(65, 91)}
    cnt = 0
    
    # 가장자리에서 BFS 시작 가능한 위치 추가
    for i in range(h):
        for j in range(w):
            if (i == 0 or j == 0 or i == h - 1 or j == w - 1):  # 가장자리 확인
                if arr[i][j] == '.' or arr[i][j] == '$' or arr[i][j].lower() in keys:
                    q.append((i, j))
                    visited[i][j] = True
                elif 'A' <= arr[i][j] <= 'Z':  # 문을 만났을 때
                    doors[arr[i][j]].append((i, j))  # 열쇠 없으면 doors에 저장
                elif arr[i][j].islower():  # 열쇠를 바로 얻을 수 있음
                    keys.add(arr[i][j])
                    q.append((i, j))
                    visited[i][j] = True

    while q:
        cx, cy = q.popleft()
        
        if arr[cx][cy] == '$':  # 문서 찾으면 카운트 증가
            cnt += 1

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] != '*':
                if 'A' <= arr[nx][ny] <= 'Z':  # 문을 만났을 때
                    if arr[nx][ny].lower() in keys:  # 열쇠가 있으면 즉시 탐색 가능
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    else:
                        doors[arr[nx][ny]].append((nx, ny))  # 열쇠 얻으면 다시 방문

                elif arr[nx][ny].islower():  # 열쇠를 발견했을 때
                    keys.add(arr[nx][ny])  # 열쇠 추가
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    
                    # 해당 열쇠로 열 수 있는 모든 문 다시 탐색
                    upper_door = arr[nx][ny].upper()
                    if doors[upper_door]:  # 열 수 있는 문이 있으면 큐에 추가
                        while doors[upper_door]:  
                            q.append(doors[upper_door].pop())
                            visited[q[-1][0]][q[-1][1]] = True

                else:  # 빈 공간 또는 문서일 경우
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())

    # 패딩 없이 입력 받기
    arr = [list(input().strip()) for _ in range(h)]
    
    # 방문 배열 (패딩 없음)
    visited = [[False] * w for _ in range(h)]
    
    # 열쇠 입력
    keys_input = input().strip()
    keys = set() if keys_input == "0" else set(keys_input)

    # BFS 실행
    print(bfs())