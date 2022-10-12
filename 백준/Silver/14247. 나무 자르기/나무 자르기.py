n = int(input())
first=list(map(int,input().split()))
len = list(map(int,input().split()))
fl =[]
cnt = 0
for i in range(n):
    fl.append([first[i],len[i]])
fl.sort(key = lambda x:x[1])

for i in range(n):
    cnt += fl[i][0]+fl[i][1]*i
print(cnt)