n = input()
cnt=[]

for i in n:
    cnt.append(n)
    n = n[1:]


for i in sorted(cnt):
    print(i)
    