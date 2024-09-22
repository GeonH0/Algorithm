
def check_bingo():
    bingo = 0
    for row in result:
        if sum(row) == 5:
            bingo += 1
    for col in range(5):
        if sum(result[row][col] for row in range(5)) == 5:
            bingo +=1

    if sum(result[i][i] for i in range(5)) == 5:
        bingo += 1
    
    if sum(result[i][4 - i] for i in range(5)) == 5:
        bingo += 1
    
    return bingo    


my = [list(map(int,input().split())) for _ in range(5)]
ans = [list(map(int,input().split())) for _ in range(5)]

result = [[0 for _ in range(5)] for _ in range(5)]


ans_dict = {}
for x in range(5):
    for y in range(5):
        ans_dict[my[x][y]] = (x, y)

cnt = 0

for i in range(5):
    for j in range(5):
        cnt +=1
        number = ans[i][j]
        x,y = ans_dict[number]

        result[x][y] = 1
        if check_bingo() >=3:
            print(cnt)
            exit()




