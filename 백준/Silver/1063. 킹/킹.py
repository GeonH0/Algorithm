

K,D,N = input().split()




king_x = int(ord(K[0])) - int(ord('A')) + 1
king_y = int(K[1])

rock_x = int(ord(D[0])) - int(ord('A')) + 1
rock_y = int(D[1])

move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(N)):
    m = input()

    nx = king_x + move[m][0]
    ny = king_y + move[m][1]

    if 0<nx<=8 and 0<ny<=8:

        if nx == rock_x and ny == rock_y:
            sx = rock_x + move[m][0]
            sy = rock_y + move[m][1]

            if 0 < sx <=8 and 0<sy<=8:
                king_x = nx
                king_y = ny
                rock_x = sx
                rock_y = sy
        else:
            king_x = nx
            king_y = ny
print(f'{chr(king_x + 64)}{king_y}')
print(f'{chr(rock_x + 64)}{rock_y}')