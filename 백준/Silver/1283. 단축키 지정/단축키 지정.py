keyword = {}

N = int(input())

for _ in range(N):
    word = input().rstrip()
    words = word.split()  # 단어를 공백 기준으로 분리
    check = False

    # 먼저 각 단어의 첫 글자를 차례로 확인
    for i in range(len(words)):
        if words[i][0].lower() not in keyword:
            # 첫 글자가 사용되지 않은 경우
            keyword[words[i][0].lower()] = 1
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            check = True
            break

    # 모든 단어의 첫 글자가 이미 사용된 경우, 나머지 글자를 확인
    if not check:
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][j].lower() not in keyword:
                    # 나머지 글자 중에서 사용되지 않은 글자를 찾음
                    keyword[words[i][j].lower()] = 1
                    words[i] = words[i][:j] + "[" + words[i][j] + "]" + words[i][j + 1:]
                    check = True
                    break
            if check:
                break

    # 모든 글자가 이미 사용된 경우 그대로 출력
    print(" ".join(words))