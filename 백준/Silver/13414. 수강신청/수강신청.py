


K,L = map(int,input().split())
dict = {}

for i in range(L):
    dict[input().rstrip()] = i

s_dict = sorted(dict.items(), key = lambda x: x[1])

for i in range(K):
    if i < len(s_dict):
        print(s_dict[i][0])
    else:
        break