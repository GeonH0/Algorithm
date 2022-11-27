a= ['c=','c-','dz=','d-','lj','nj','s=','z=',]
alp = input()

for i in a:
    alp = alp.replace(i,'1')
print(len(alp))