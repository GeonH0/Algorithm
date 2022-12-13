



n = str(input())
ok =0

for i in range(1,len(n)):
    s1,s2= n[:i],n[i:]
    m1=m2=1
    for i in s1:
        m1*=int(i)
    for j in s2:
        m2 *=int(j)
    if m1 ==m2:
        ok =1
        break
print("YES" if ok else "NO")





    