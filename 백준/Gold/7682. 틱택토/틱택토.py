
def check(board, player):
    # player가 이겼는지 확인
    for row in board:
        if row[0] == row[1] == row[2] and row[0] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] == player:
        return True
    return False


while True:
    arr = input().rstrip()
    
    if arr == 'end':
        break
    board = [arr[i:i+3] for i in range(0,9,3)]
    x_cnt = arr.count('X')
    o_cnt = arr.count('O')

    x_win = check(board, 'X')
    o_win = check(board, 'O')
    if o_cnt > x_cnt or x_cnt > o_cnt + 1:
        print("invalid")
    elif x_win and o_win:
        print("invalid")
    elif x_win and x_cnt != o_cnt + 1:
        print("invalid")
    elif o_win and x_cnt != o_cnt:
        print("invalid")
    elif not x_win and not o_win and x_cnt + o_cnt != 9:
        print("invalid")
    else:
        print("valid")    
        

            
