a=[]
c=0
for i in range(10):
    a.append(int(input()))
for j in a:
    c+=j
    if c>=100:
        if c-100>100-(c-j):
            c-=j
        break
print(c)
