s=[0]*10
n= input()
for i in str(n):
    if i=='9' or i=='6':
        if s[6]==s[9]:
            s[6]+=1
        else:
            s[9]+=1
    else:
        s[int(i)]+=1
print(max(s))
