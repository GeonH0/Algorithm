import sys
input = sys.stdin.readline


N =int(input())
print("*"* N + " "*(2*N-3)+"*" * N)

for i in range(1,N-1):
    print(" "* i + "*" + " " *(N-2) + "*" + " "*(2*(N-i)-3) + "*" + " "* (N-2)+ "*" )

print(" "*(N-1) + "*" + " " * (N-2)+ "*" + " " * (N-2) + "*")

for i in range(N-2,0,-1):
    print(" "* i + "*" + " " *(N-2) + "*" + " "*(2*(N-i)-3) + "*" + " "* (N-2)+ "*" )
print("*"* N + " "*(2*N-3)+"*" * N)