from collections import deque



n= int(input())
arr= deque(enumerate(map(int,input().split())))
cnt =[]

while arr:
    idx,num = arr.popleft()
    cnt.append(idx+1)
    if num>0:
        arr.rotate(-(num-1))
    elif num<0:
        arr.rotate(-num)
print(" ".join(map(str,cnt)))