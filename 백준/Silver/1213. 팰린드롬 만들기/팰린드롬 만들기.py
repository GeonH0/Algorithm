
from typing import Counter


word = list(map(str,input().rstrip()))
word.sort()
check = Counter(word)

cnt = 0
center = ""
for i in check:
    # 만약 문자열이 홀수개일 경우
    if check[i] % 2 != 0:
        #홀수 갯수 1개 count 후 센터 자리에 해당 문자 추가
        #원래 문자에서 해당 문자 삭제
        cnt +=1
        center +=i
        word.remove(i)
    # 홀수개인 문자가 2개 이상일 경우 성립 불가
    if cnt>1:        
        break
if cnt >1:
    print("I'm Sorry Hansoo")
else:
    ans = ""
    for i in range(0,len(word),2):
        #만약 반을 나왔다면
        ans += word[i]
    print(ans + center + ans[::-1])


    