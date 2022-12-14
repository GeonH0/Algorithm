s = int(input())
em =  input()
h,I,a,r,c=0,0,0,0,0

for i in em:
    if i=='H':
        h +=1
    elif i=='I':
        I +=1
    elif i=='A':
        a+=1
    elif i=='R':
        r+=1
    elif i=='C':
        c+=1
print(min(h,I,a,r,c))


