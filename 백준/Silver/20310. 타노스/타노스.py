# 입력 문자열 받기
s = input().strip()

# 0과 1의 개수를 세기
zero_count = s.count('0') // 2  # 남겨야 할 '0'의 개수
one_count = s.count('1') // 2  # 남겨야 할 '1'의 개수

# 결과 생성
result = '0' * zero_count + '1' * one_count

# 출력
print(result)
