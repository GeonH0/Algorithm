


N,M = map(int,input().split())
K = int(input())
arrN,arrM = [0,N],[0,M]
maxN,maxM = 0,0
for _ in range(K):
    a,b = map(int,input().split())
    if a == 0:
        arrM.append(b)
        
    if a == 1:
        arrN.append(b)
        
arrM.sort()
arrN.sort()
for i in range(1,len(arrM)):
    maxM = max(maxM,arrM[i]-arrM[i-1])
for i in range(1,len(arrN)):
    maxN = max(maxN,arrN[i]-arrN[i-1])
print(maxM*maxN)