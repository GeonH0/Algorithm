








#dr : 북 동 남 서(왼쪽방향으로 회전)
di=[-1,0,1,0]
dj = [0,1,0,-1]

def solve(ci,cj,dr):
    cnt =0

    while True: # 청소기가 더이상 움직이지 못할경우 종료
        #현재 위치 청소
        arr[ci][cj]=2
        cnt +=1

        #왼쪽방향으로 순서대로 탐색해서 미청소 영역이 있는경우 이동
        fl = 1
        while fl:
            #왼쪽 부터 4 방향중 미청소 영역이 있는경우
            for i in ((dr+3)%4,(dr+2)%4,(dr+1)%4,dr):
                ni,nj = ci+di[i],cj+dj[i]
                if arr[ni][nj] ==0: #청소가 안된 영역일경우
                    ci,cj,dr = ni,nj,i
                    fl = 0
                    break
            else: # 4방향 모두 미청소 영역 없음 -> 후진(벽체크)
                bi,bj = ci-di[dr],cj-dj[dr] #후진할 위치 게산
                if arr[bi][bj]==1: #벽일경우 종료
                    return cnt
                else: #후진하기
                    ci,cj = bi,bj
        


        



N,M = map(int,input().split())
R,C,D= map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]

ans = solve(R,C,D)
print(ans)