n = int(input())
st = input()
a=[0]*n

for i in range(n):
    a[i]= int(input())
stack = []

for i in st:
    if 'A' <= i <= 'Z':
        stack.append(a[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])