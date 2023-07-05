

def check(loc,dis):
    if loc ==1: #북
        return dis
    elif loc ==4:#동
        return w+dis
    elif loc ==2:#남
        return w+h+w -dis
    elif loc ==3: #tj
        return w+h+w+h-dis
    
w,h = map(int,input().split())
num = (int(input()))

store = [0]*(num+1)
arr=[]

for i in range(num+1):
    l,d = map(int,input().split())
    arr.append(check(l,d))

dong_arr=arr[-1]# 마지막은 동근이의 위치
cnt =0

for i in range(num):
    cal_distance=abs(arr[i]-dong_arr)
    t = 2*(w+h)
    cnt += min(cal_distance,t-cal_distance)

print(cnt)
