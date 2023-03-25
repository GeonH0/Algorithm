from itertools import permutations


n = int(input())

data = ['1','2','3','4','5','6','7','8','9']
num = list(permutations(data,3))

for _ in range(n):
    a,s,b = map(int,input().split())
    a = list(str(a))
    cnt =0

    for i in range(len(num)):
        st = ba =0
        i-= cnt
        for j in range(3):
            if num[i][j] == a[j]:
                st+=1
            elif a[j] in num[i]:
                ba+=1
        if (st!=s) or (ba!=b):
            num.remove(num[i])
            cnt+=1
print(len(num))