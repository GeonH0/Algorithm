W = list(input().rstrip())

i=0 
start = 0

while i<len(W):
    if W[i]=='<':
        i+=1
        while W[i] !='>':
            i+=1
        i+=1
    elif W[i].isalnum():
        start= i
        while i< len(W) and W[i].isalnum():
            i+=1
        temp = W[start:i]
        temp.reverse()
        W[start:i]=temp
    else:
        i+=1
print("".join(W))