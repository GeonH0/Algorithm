n = list(map(int,(input().rstrip())))
cnt =0


while len(n)>1:
    cnt +=1
    tmp =[]
    n = sum(n)
    for i in str(n):
        tmp.append(int(i))

    n = tmp
print(cnt)

if n[0]%3==0:
    print("YES")
else:
    print("NO")