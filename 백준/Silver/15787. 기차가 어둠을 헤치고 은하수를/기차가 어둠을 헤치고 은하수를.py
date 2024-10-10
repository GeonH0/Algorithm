def shift_left(arr):    
    for i in range(19):
        arr[i] = arr[i+1]
    arr[19] = 0

def shift_right(arr):
    for i in range(19, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = 0

N,M = map(int,input().split())

train = [[0]*20 for _ in range(N)]
history = set()

for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        if train[command[1]-1][command[2]-1]  == 0:
            train[command[1]-1][command[2]-1] = 1            
    elif command[0] == 2:
        if train[command[1]-1][command[2]-1] == 1:
            train[command[1]-1][command[2]-1] = 0
    elif command[0] == 3:
        shift_right(train[command[1]-1])
    elif command[0] == 4:
        shift_left(train[command[1]-1])

for t in train:
    state = tuple(t)
    history.add(state)
    
print(len(history))