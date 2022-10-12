n = int(input())
cnt = 0
pay =[]
for i in range(n):
    pay.append(int(input()))

pay.sort(reverse=True)
for i in range(n):
    if i%3 !=2:
        cnt+=pay[i]
print(cnt)