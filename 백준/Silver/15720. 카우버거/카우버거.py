

B,C,D = map(int,input().split())
bur = list(map(int,input().split()))
side = list(map(int,input().split()))
coke = list(map(int,input().split()))
ans = 0
bur.sort(reverse=True)
side.sort(reverse=True)
coke.sort(reverse=True)

print(sum(bur)+sum(side)+sum(coke))
print(int((sum(bur[:min(B,C,D)])+sum(side[:min(B,C,D)])+sum(coke[:min(B,C,D)]))*0.9) + (sum(bur[min(B,C,D):])+sum(side[min(B,C,D):])+sum(coke[min(B,C,D):])))
