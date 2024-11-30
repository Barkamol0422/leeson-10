a,b=map(int,input('Write two numbers: ').split())
c=0
for i in range(1,b+1,a):
    c=a**i
    print(c)