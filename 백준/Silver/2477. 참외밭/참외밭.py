
import sys
input = sys.stdin.readline

arr1=[]
arr2=[]
total =[]

n = int(input())

for _ in range(6):
    a,b = map(int,input().split())
    if a == 1 or a ==2:
        arr1.append(b)
        total.append(b)
    else:
        arr2.append(b)
        total.append(b)

bigbox = max(arr1)*max(arr2)

maxhidx = total.index(max(arr1))

maxwidth = total.index(max(arr2))

small1 = abs(total[maxhidx-1]-total[(maxhidx-5 if maxhidx ==5 else maxhidx +1)])
small2 = abs(total[maxwidth-1]-total[(maxwidth-5 if maxwidth ==5 else maxwidth +1)])                            
print((bigbox-(small1*small2))*n)                                
