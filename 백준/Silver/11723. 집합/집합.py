import sys
input= sys.stdin.readline


s= set()

m = int(input())

for i in range(m):
    a = input().split()
    if len(a)==1:
        if a[0]=='all':
            s= set([x for x in range(1,21)])
        else:
            s= set()
    else:
        c,d = a[0],int(a[1])

        if c =='add':
            s.add(d)
        elif c == 'check':
            if d in s:
                print(1)
            else:
                print(0)

        elif c== 'remove':
            if d in s:
                s.discard(d)

        elif c=='toggle':
            if d in s:
                s.discard(d)
            else:
                s.add(d)
        
                
                
