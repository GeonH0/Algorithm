

cnt =1
N = int(input())
ans = []
arr =[]
check = True
for _ in range(N):
    num = int(input())

    while cnt <= num:
        ans.append(cnt)
        arr.append('+')
        cnt +=1
    if ans[-1] == num:
        ans.pop()
        arr.append('-')
    else:
        check = False
        break
if check == False:
    print("NO")
else:
    for i in arr:
        print(i)

