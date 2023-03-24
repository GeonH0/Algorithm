import sys
input = sys.stdin.readline

cnt =0.0
an =0.0

for _ in range(0,20,1):
    a,b,c = map(str,input().split())

    d = float(b)
    
    if c == 'A+':
        an +=d
        cnt += float(d*(4.5))
    elif c == 'A0':
        an +=d
        cnt += float(d*(4.0))
    elif c == 'B+':
        an +=d
        cnt += float(d*(3.5))
    elif c == 'B0':
        an +=d
        cnt += float(d*(3.0))
    elif c == 'C+':
        an +=d
        cnt += float(d*(2.5))
    elif c == 'C0':
        an +=d
        cnt += float(d*(2.0))
    elif c == 'D+':
        an +=d
        cnt += float(d*(1.5))
    elif c == 'D0':
        an +=d
        cnt += float(d*(1.0))
    elif c == 'F':
        an +=d
        cnt += float(d*(0.0))
    elif c == 'P':
        continue
ans = round((cnt/ an),6)
print(f"{ans}")
    

