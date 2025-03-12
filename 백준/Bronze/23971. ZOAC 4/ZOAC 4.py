

from math import ceil


H,W,N,M = map(int,input().split())

print(ceil(W/(M+1))*ceil(H/(N+1)))
