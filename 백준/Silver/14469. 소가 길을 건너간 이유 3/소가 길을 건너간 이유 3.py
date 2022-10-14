n = int(input())
a=[]
time =0
for i in range(n):
    s,t=map(int,input().split())
    a.append([s,t])
a.sort(key = lambda x:x[0])

for j in range(len(a)):
    if time > a[j][0]:
        time = time +a[j][1]
    else:
        time =a[j][0]+a[j][1]

print(time)
