

n,m= map(int,input().split())
word = [input() for _ in range(n)]
check = [input() for _ in range(m)]
cnt =0

for i in range(m):
    for j in range(n):
        if word[j].startswith(check[i]):
            cnt +=1
            break        
print(cnt)        