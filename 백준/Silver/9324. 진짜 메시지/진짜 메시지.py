

T = int(input())

for _ in range(T):
    M = input()
    msg,res = [0 for _ in range(26)],"OK"
    c = False
    for i in range(len(M)):
        if c:
            c = False
            continue
        msg[ord(M[i])-65] +=1
        if msg[ord(M[i])-65] == 3:
            if i == len(M)-1:
                res = "FAKE"
                break
            elif M[i] != M[i+1]:
                res = "FAKE"
                break
            c = True
            msg[ord(M[i])-65] = 0
    print(res)
            

    
        
