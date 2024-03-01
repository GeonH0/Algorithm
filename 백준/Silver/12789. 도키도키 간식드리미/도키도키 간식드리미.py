




N = int(input())

arr = list(map(int,input().split()))
stack = []
cur = 1



while arr:
    if arr[0] == cur:
        arr.pop(0)
        cur +=1
    else:
        stack.append(arr.pop(0))
    
    while stack:
        if stack[-1] == cur:
            stack.pop()
            cur +=1
        else:
            break

if len(stack)  == 0:
    print("Nice")
else:
    print("Sad")