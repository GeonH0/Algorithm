
S = input()

revers = ""
ans = ""
is_Tag = False
for i in S:    
    if i =="<":
        if revers:
            ans += revers[::-1]
            revers = ""
        ans += i
        is_Tag = True
    elif i == ">":
        ans +=i
        is_Tag = False
    elif is_Tag:
        ans +=i
    else:
        if i != " ":
            revers += i
        else:
            ans += revers[::-1] + " "
            revers = ""
if revers:
    ans += revers[::-1]    
    
print(ans)