





R = input().upper()
Rlist = list(set(R))
cnt =[]

for i in Rlist:
    count = R.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(Rlist[(cnt.index(max(cnt)))])