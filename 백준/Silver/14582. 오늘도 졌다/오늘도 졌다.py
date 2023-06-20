a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt =0
a_c =0
b_c=0
for i in range(len(a)):

    a_c += a[i]
    if a_c > b_c and cnt == 0:
        cnt += 1
    if a_c> b_c and cnt ==1:
        cnt +=1
    b_c +=b[i]            

if cnt ==2 and a_c< b_c or cnt ==1 and a_c<b_c:
    print("Yes")
else:
    print("No")
        
 
    
