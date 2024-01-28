import sys
input = sys.stdin.readline

N = input().strip()
M = int(input())
command = []

for _ in range(M):
    command.append(input().strip())
left = list(N)
right = []

for i in command:
    c = i.split()
    action = c[0]
    if action == "L":
        if left:
            right.append(left.pop())
    elif action == "D":
        if right:
            left.append(right.pop())
    elif action == "B":
        if left:
            left.pop()
    elif action == "P":
        left.append(c[1])

ans = left + right[::-1]
print("".join(ans))
