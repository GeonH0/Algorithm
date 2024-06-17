N = int(input())
monster = []
needcandy = [] # 포켓몬이 진화에 필요한 사탕의 수
havecandy = [] # 총 사탕수
cnt = []

for _ in range(N):
    tmp = 0
    monster.append(str(input()))
    a,b  = map(int,input().split())
    needcandy.append(a)
    havecandy.append(b)
    while b >= a:
        b = b - a + 2
        tmp += 1
    cnt.append(tmp)

max_cnt = max(cnt)
max_index = cnt.index(max_cnt)
print(sum(cnt))
print(monster[max_index])


    



