


n,m = map(int,input().split())
HD=[]
cnt =0
result=''
for i in range(n):
    HD.append(input())

for j in range(m):
    count = [0,0,0,0]
    for k in range(n):
        if HD[k][j]=='A':
            count[0]+=1
        elif HD[k][j]=='C':
            count[1]+=1    
        elif HD[k][j]=='G':
            count[2]+=1
        elif HD[k][j]=='T':
            count[3]+=1
    idx = count.index(max(count))
    if idx ==0:
        result +='A'
    elif idx==1:
        result +='C'
    elif idx==2:
        result +='G'
    elif idx==3:
        result +='T'
    cnt += n-max(count)

print(result)
print(cnt)


