n = int(input())
roads  =list(map(int,input().split()))
cities = list(map(int,input().split()))

minVal = cities[0] #첫도시의 기름 값을 먼저 minVal로 설정
sum =0
for i in range(n-1):
    if minVal>cities[i]: # minVal보다 싼 citie가 발견되 결ㅇ우
        minVal = cities[i] # 그값을 minVal로 변경
    sum +=(minVal*roads[i]) #도로 길이를 곱한 값을 sum에 더한다.
print(sum)