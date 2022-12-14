


a,b,c = map(int,input().split())
x,y,z =map(int,input().split())
cnt=0
for i in range(3):
    chicken = min(a,x)
    cnt += chicken
    a-=chicken
    x-=chicken
    pizza =min(b,y)
    cnt +=pizza
    b-=pizza
    y-=pizza
    burger=min(c,z)
    cnt +=burger
    c-=burger
    z-=burger
    y,z,x = x//3,y//3,z//3
print(cnt)
