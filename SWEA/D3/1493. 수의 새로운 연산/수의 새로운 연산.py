T = int(input())

i,j =1,1
dct ={}
re_dct={}
for n in range(1,50000):
    dct[n] = (i,j)
    re_dct[(i,j)] = n
    i,j = i-1,j+1
    if i <1:
        i = j
        j = 1

for test_case in range(1,T+1):
    p,q = map(int,input().split())
    pi,pj = dct[p]
    qi,qj = dct[q]
    ans = re_dct[(pi+qi,pj+qj)]
    print(F"#{test_case} {ans}")

    