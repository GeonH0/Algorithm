n = int(input())
s=[]
a,b = map(int,input().split())
c= int(input())

for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)

answer = c/a

for j in range(1, len(s)+1):
    cal = c+sum(s[0:j])
    pr = a+(b*j)

    if cal/pr >answer:
        answer = cal/pr
    else:
        break
print(int(answer))