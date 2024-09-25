def flip_bit(b):
    return b ^ 1

N = int(input())

status = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    s, num = map(int, input().split())
    if s == 1:
        # 남학생의 경우
        for i in range(len(status)):
            if (i + 1) % num == 0:
                status[i] = flip_bit(status[i])
    elif s == 2:
        # 여학생의 경우
        for j in range(1, min(num, len(status) - num + 1)):
            if num - 1 - j >= 0 and num - 1 + j < len(status):
                if status[num - 1 - j] == status[num - 1 + j]:
                    status[num - 1 - j] = flip_bit(status[num - 1 - j])
                    status[num - 1 + j] = flip_bit(status[num - 1 + j])
                else:
                    break
        status[num - 1] = flip_bit(status[num - 1])

for i in range(0, len(status), 20):
    print(" ".join(map(str, status[i:i+20])))