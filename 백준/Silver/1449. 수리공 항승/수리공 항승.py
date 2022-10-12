n,l = map(int,input().split())
s = list(map(int,input().split()))
s.sort()

start = s[0]
cnt =1

for i in s[1:]:
    if i in range(start,start+l): #범위 안에 들어오면 기존 테이프 사용
        continue
    else:
        start = i # 범위 밖이면 새 테이프를 사용 하고 테이프 갯수를 추가한다
        cnt +=1
print(cnt)