import sys
input = sys.stdin.readline


N,K = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(float(input()))
    
arr.sort()

    


print('{:.2f}'.format(sum(arr[K:N-K])/float(N-2.0*K)+1e-8))
print('{:.2f}'.format((sum(arr[K:N-K])+arr[K]*K+arr[N-K-1]*K)/N + 1e-8))







