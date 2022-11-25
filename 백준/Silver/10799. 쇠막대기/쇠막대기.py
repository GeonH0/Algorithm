b = list(input())
a =0
st=[]

for i in range(len(b)):
    if b[i]=='(':
        st.append('(')
    else:
        if b[i-1]=='(':
            st.pop()
            a += len(st)
        else:
            st.pop()
            a+=1
print(a)