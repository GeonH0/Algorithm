n = int(input())
da= int(input())
a=[]
cnt =0
for i in range(n-1):
    a.append(int(input()))
a.sort(reverse=True)
if(n==1):
    print(0)
else:
    while a[0]>=da:
        da+=1
        a[0]-=1
        cnt +=1
        a.sort(reverse=True)
    print(cnt)