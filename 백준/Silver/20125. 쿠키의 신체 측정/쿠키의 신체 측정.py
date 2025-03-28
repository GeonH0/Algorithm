
def src(x,y):
    left,right,line,leftfoot,rightfoot =0 ,0,0,0,0
    waist_end = 0
    
    for i in range(N):
        if arr[x+1][i] == "*" and i < y:
            left +=1
        elif arr[x+1][i] == "*" and i > y:
            right +=1

    for j in range(x+2,N):        
        if arr[j][y] == "*":
            line +=1
            waist_end = j
        else:
            break
    

    for i in range(waist_end + 1, N):        
        if y - 1 >= 0 and arr[i][y - 1] == "*":
            leftfoot += 1
        if y + 1 < N and arr[i][y + 1] == "*":
            rightfoot += 1
                
        
            

            

    return left,right,line,leftfoot,rightfoot
        

N = int(input())
arr =[input().rstrip() for _ in range(N)]

head = False
headx,heady = 0,0
heartx,hearty = 0,0

for i in range(N):
    for j in range(N):
        if arr[i][j] == "*" and head == False:
            headx = i
            heady = j
            
            head = True
            print(i+2,j+1)
            print(" ".join(map(str,src(i,j))))  



