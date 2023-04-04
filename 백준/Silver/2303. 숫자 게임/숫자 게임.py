n= int(input()) #사람의 수

arr=[]
for _ in range(n):
    c = (list(map(int,input().split()))) #각 카드의 수
    max_num = 0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                num = (c[i]+c[j]+c[k])%10 #3장식 뽑아서 더한수 1의자리 구하기

                if num>max_num:
                    max_num = num

    arr.append(max_num) # max숫자를 배열에 입력

for i in range(n-1,-1,-1): # 큰 번호부터 배열 돌기
    if arr[i]==max(arr): # 제일 큰 수 찾기
        print(i+1) #인덱스 +1 로 출력
        break
    