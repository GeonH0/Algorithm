
import sys

from typing import Counter
input = sys.stdin.readline

n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()

print(round(sum(arr)/n))

print(arr[n//2])
cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
print(max(arr)-min(arr))