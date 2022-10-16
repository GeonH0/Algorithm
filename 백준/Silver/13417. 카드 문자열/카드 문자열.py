n = int(input())

for i in range(n):
    m=int(input())
    a=list(map(str,input().split()))
    s=[a[0]]

    for j in range(1,len(a)):
        left = s[0]

        if a[j]<=left:
            s.insert(0,a[j])
        else:
            s.append(a[j])
    
    print(''.join(s))