n = input()
cnt = set()
for i in range(len(n)):
    for j in range(i,len(n)):
        temp =n [i:j+1]
        cnt.add(temp)

print(len(cnt))

