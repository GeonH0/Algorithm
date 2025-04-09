from collections import Counter


def is_similar(w1, w2):
    c1 = Counter(w1)
    c2 = Counter(w2)

    diff1 = c1 - c2
    diff2 = c2 - c1

    total_diff = sum(diff1.values()) + sum(diff2.values())

    if len(w1) == len(w2):
        # 길이가 같으면 → '바꾸기'만 허용
        return total_diff <= 2
    elif abs(len(w1) - len(w2)) == 1:
        # 길이 차이가 1 → 추가 or 삭제
        return total_diff == 1
    else:
        return False

N = int(input())
arr = list(input().rstrip() for _ in range(N))

cnt = 0
ans = Counter(arr[0])

for i in range(1,N):
    if is_similar(arr[0],arr[i]):
        cnt +=1
print(cnt)