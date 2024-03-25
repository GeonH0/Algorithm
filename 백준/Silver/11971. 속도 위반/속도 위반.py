

N,M = map(int,input().split())
street = []
move = []
for i in range(N):
    a,b = map(int,input().split())
    for j in range(a):
        street.append(b)

for i in range(M):
    a,b = map(int,input().split())
    for j in range(a):
        move.append(b)

tmp = 0


for i in range(100):
    if move[i] - street[i] >tmp:
        tmp = move[i] - street[i]
print(tmp)
    
    