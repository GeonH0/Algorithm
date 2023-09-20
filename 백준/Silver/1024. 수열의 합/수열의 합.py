

N,L = map(int,input().split())

for i in range(L,101):
    xi = N-(i*(i+1)//2)
    if xi %i ==0:
        x = xi //i
        if x +1>=0:
            for j in range(x+1,x+i+1):
                print(j,end = " ")
            break
else:
    print(-1)