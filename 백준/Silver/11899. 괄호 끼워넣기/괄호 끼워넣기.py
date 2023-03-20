


s = input().rstrip()
st=[]
cnt=0

for i in s:
    if i =='(':
        st.append(i)
    else:
        if st and st[-1]=='(':
            st.pop()
        else:
            st.append(i)


print(len(st))