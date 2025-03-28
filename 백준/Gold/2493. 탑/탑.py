



N = int(input())

arr = list(map(int,input().split()))
st = []
ans = [0] * N

for i in range(N):
    while st and arr[st[-1]] < arr[i]:
        st.pop()
    
    if st:
        ans[i] = st[-1] + 1
    else:
        ans[i] = 0
    st.append(i)
    

print(' '.join(map(str,ans)))
