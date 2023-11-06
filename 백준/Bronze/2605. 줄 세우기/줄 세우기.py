


N = int(input())
answer = []
for i in range(1,N+1):
    answer.append(i)
arr= list(map(int,input().split()))

for i in range(N):
    n,t = arr[i],answer[i] #몇칸 앞?, 현재 칸
    #덮어씌우기
    for j in range(i,i-n,-1):
        answer[j] = answer[j-1]
    answer[i-n] = t
print(*answer)

