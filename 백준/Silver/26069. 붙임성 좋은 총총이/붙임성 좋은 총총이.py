n = int(input())
c=['ChongChong']
for i in range(n):
    a,b = input().split()
    if a in c:
        if b in c:
            continue
        else:
            c.append(b)
    elif b in c:
        if a in c:
            continue
        else:
            c.append(a)
print(len(c))
        