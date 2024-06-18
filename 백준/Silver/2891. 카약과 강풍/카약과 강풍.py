N, S, R = map(int, input().split())
arrS = list(map(int, input().split()))
arrR = list(map(int, input().split()))

# 중간에 제거하지 않고, 먼저 같은 번호를 제외한 뒤 인접한 번호를 고려하도록 변경
same = set(arrR).intersection(set(arrS))

# 같은 번호 제거
for s in same:
    arrS.remove(s)
    arrR.remove(s)

# 인접한 번호 처리
for i in arrR[:]:
    for j in arrS[:]:
        if i + 1 == j or i - 1 == j:            
            arrS.remove(j)
            arrR.remove(i)
            break  # 리스트를 수정했으므로 내부 루프를 탈출
print(len(arrS))