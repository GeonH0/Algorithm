n = int(input())
cnt =0
for i in range(n):
    x = input()
    x = x[2:]
    if(int(x)<=90):
        cnt +=1
print(cnt)
