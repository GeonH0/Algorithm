n,m = map(int,input().split())
og=[]
cnt =[]
for _ in range(n):
    og.append(input())
for i in range(n-7):
    for j in range(m-7):
        idx1=0
        idx2=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(k+l)%2==0:
                    if og[k][l] !='W':
                        idx1+=1
                    if og[k][l] != 'B':
                        idx2+=1
                else:
                    if og[k][l] !='B':
                        idx1+=1
                    if og[k][l] !='W':
                        idx2+=1
        cnt.append(min(idx1,idx2))
print(min(cnt))