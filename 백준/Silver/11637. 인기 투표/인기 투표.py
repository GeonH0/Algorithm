
import sys
input = sys.stdin.readline

T = int(input())
arr=[]
m =[]
for _ in range(T):
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    
    mv = max(arr)
    mc = arr.count(mv)
    t = sum(arr)
    if mc > 1:
        print("no winner")
        arr=[]
    else:
        if mv > t/2:
            print("majority winner", arr.index(mv) + 1)  # 절대 다수인 경우
            arr=[]
        else:
            print("minority winner", arr.index(mv) + 1)  # 절대 다수가 아닌 경우
            arr=[]



