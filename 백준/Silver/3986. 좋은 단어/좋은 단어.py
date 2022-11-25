n = int(input())
cnt =0
for _ in range(n):
    l = input().rstrip()
    s=[]

    for i in range(len(l)):
        if s and l[i]==s[-1]:
            s.pop()
        else:
            s.append(l[i])

    if not s:
        cnt +=1

print(cnt)