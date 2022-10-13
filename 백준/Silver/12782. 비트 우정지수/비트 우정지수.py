
n = int(input())
cnt =0

for i in range(n):
    a,b  = input().split()
    c1=0
    c2=0
    for j in range(len(a)):
        if a[j] !=b[j]:
            if a[j]=='1':
                c1+=1
            else:
                c2 +=1
    print(max(c1,c2))            