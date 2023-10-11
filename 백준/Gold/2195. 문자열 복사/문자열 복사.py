


S =  input().rstrip()
P = input().rstrip()

ans = 0
start =0
end =0
while True:
    if start == len(P):
        break
    for i in range(len(S)-(end-start)):
        if S[i:i+(end-start)+1] == P[start:end+1]:
            end +=1
            break
    else:
        ans +=1
        end -=1
        start = end +1
        end = start
print(ans) 
