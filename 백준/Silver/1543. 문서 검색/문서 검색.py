from cmath import pi


n = input()
m = input()
cnt =0
i=0
while i <= len(n)-len(m):
    if n[i:i +len(m)]==m:
        cnt +=1
        i+=len(m)
    else:
        i+=1
print(cnt)
