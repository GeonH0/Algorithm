n,m = map(int,input().split())

start = 1
end = m
apple =[]
cnt=0
j = int(input())
for _ in range(j):
    apple.append(int(input()))

for i in range(j):
    if(end>=apple[i] and start <=apple[i]):
        continue
    elif (end <apple[i]):
        cnt +=apple[i]-end
        end = apple[i]
        start = apple[i]-(m-1)
    elif (start>apple[i]):
        cnt += start-apple[i]
        start=apple[i]
        end =apple[i]+(m-1)

print(cnt)