a=[]
for i in range(9):
    a.append(int(input()))
h = sum(a)

for j in range(8):
    for k in range(j+1,9):
        if h -a[j]-a[k]==100:
            f1,f2 = a[j],a[k]
            a.remove(f1)
            a.remove(f2)
            for t in a:
                print(t)
            break
    if len(a) ==7:
        break
