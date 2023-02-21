num = set(range(1,10001))

n = set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    n.add(i)
s_num = sorted(num-n)
for i in s_num:
    print(i)