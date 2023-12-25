

N1,N2 = map(int,input().split())
arr1 = list(map(str,input().rstrip("\n")))
arr2 = list(map(str,input().rstrip("\n")))
t = int(input())

arr1.reverse()
total = arr1+arr2

for _ in range(t):
    for i in range(len(total)-1):
        if total[i] in arr1 and total[i+1] in arr2:
            total[i],total[i+1] = total[i+1],total[i]

            if total[i+1] == arr1[-1]:
                break
print("".join(total))
