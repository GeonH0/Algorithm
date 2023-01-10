n = int(input())
arr=[]
temp = [] 
cnt =[]
for i in range(n):
    arr.append(i+1)

while(len(arr)!=0):
    if(len(arr)==1):
        cnt.append(arr[0])
        break
    cnt.append(arr[0])
    del arr[0]
    
    arr.append(arr[0])
    
    del arr[0]
    
for i in cnt:
    print(i,end=" ")

