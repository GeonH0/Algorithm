from tabnanny import check


N = int(input())
ans = 0

for _ in range(N):
    word = input()
    check = []
    isgroup = True
    if len(word) == 1:
        ans +=1
    else:
        check.append(word[0])
        for i in range(1,len(word)):
            if word[i] == word[i-1]:
                continue
            else:
                if word[i] not in check:
                    check.append(word[i])
                    continue
                else:
                    isgroup = False
                    break
        if isgroup:
            ans +=1
        
print(ans)
