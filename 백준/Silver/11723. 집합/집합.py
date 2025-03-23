import sys
input = sys.stdin.readline

M = int(input())
ans = set()
for _ in range(M):
    action = list(map(str,input().split()))
    if len(action) == 1:
        if action[0] == 'all':
            ans = set(range(1, 21))

        elif action[0] == 'empty':
            ans = set()
    else:
        if action[0] == 'add':
            ans.add(int(action[1]))
        elif action[0] == 'remove':
            if int(action[1]) in ans:
                ans.remove(int(action[1]))
                
            else:
                continue
        elif action[0] == 'check':
            if int(action[1]) in ans:                
                print(1)
            else:                
                print(0)
        elif action[0] == 'toggle':
            if int(action[1]) in ans:
                ans.remove(int(action[1]))
            else:
                ans.add(int(action[1]))
