def find_position(char):
    for i, row in enumerate(KEYBOARD):
        if char in row:
            return i, row.index(char)

KEYBOARD = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]

LEFT_KEYS = set("qwertasdfgzxcv")
RIGHT_KEYS = set("yuiophjklbnm")

sl, sr = input().split()
word = input()

lx, ly = find_position(sl)
rx, ry = find_position(sr)

total_time = 0

for char in word:
    nx, ny = find_position(char)
    if char in LEFT_KEYS:
        total_time += abs(lx - nx) + abs(ly - ny)
        lx, ly = nx, ny
    else:
        total_time += abs(rx - nx) + abs(ry - ny)
        rx, ry = nx, ny
    total_time += 1  # 키 입력 시간

print(total_time)