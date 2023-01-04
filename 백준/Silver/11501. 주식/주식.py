

for _ in range(int(input())):
    n = int(input())
    m=list(map(int,input().split()))
    m.reverse()
    max = m[0]
    cnt =0
    for i in range(1,n):
        if max<m[i]:
            max =m[i]
            continue
        cnt += max - m[i]    
    print(cnt)