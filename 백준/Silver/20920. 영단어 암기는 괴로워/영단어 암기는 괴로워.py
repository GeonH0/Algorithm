

# 자주 나오는 단어일수록 앞에 배치, 
# 단어의 길이가 길수록 앞에 배치, 
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 뱇

import sys


input = sys.stdin.readline
N,M = map(int,input().split())
note = {}
for _ in range(N):
    word = input().strip()
    if len(word)>=M:
        if word in note:
            note[word] += 1
        else:
            note[word] = 1

sorted_words = sorted(note.items(), key = lambda x: (-x[1],-len(x[0]),x[0]))

for i in sorted_words:
    print(i[0])
