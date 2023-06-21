n = int(input())

stars = [[' ' for _ in range(4*n-3)]for _ in range(4*n-3)]

def fil_star(n,x,y):
    if n ==1:
        stars[y][x] ='*'
        return

    ln = 4*n-3

    for i in range(ln):
        stars[y][x+i] = '*'
        stars[y+i][x] = '*'
        stars[y+ln-1][x+i] = '*'
        stars[y+i][x+ln-1] = '*'
    fil_star(n-1,x+2,y+2)

fil_star(n,0,0)
for j in stars:
    print(''.join(j))