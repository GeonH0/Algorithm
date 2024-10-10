def find_kth_lucky_number(k):
    result = ""
    while k > 0:
        if k % 2 == 0:
            result = "7" + result
        else:
            result = "4" + result
        k = (k - 1) // 2
    return result

# 입력 받기
K = int(input())

# 결과 출력
print(find_kth_lucky_number(K))