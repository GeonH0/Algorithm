n,m = map(int,input().split())


j =[]
for i in range(n):
    p,l = map(int,input().split())
    k=(list(map(int,input().split())))
    k.sort(reverse=True)
    if(p<l):
        j.append(1)
    else:
        j.append(k[l-1])
        
j.sort()
cnt = 0
for  i in j:
    m-=i
    cnt +=1
    if m<0:
        print(cnt-1)
        break
if m>0:
    print(cnt)

 
