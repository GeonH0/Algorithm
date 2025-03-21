N = str(input())
cnt = {}
for i in N.upper():
      
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] +=1

ans = max(cnt.values())
key = [k for k, v in cnt.items() if v == ans]

if len(key) > 1:
    print('?')
else:
    print(key[0])
