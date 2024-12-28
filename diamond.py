a=int(input("Enter number of rows: "))
if a%2==0:
    b=int(a/2)
else:
    b=int((b/2)+1)
c=b-1
for i in range(1,b+1):
    for j in range(1,c+1):
        print(end=" ")
    c=c-1
    d=1
    for j in range(2*i-1):
        print(end=str(d))
        d+=1
    print()
c=1
for i in range(1,b-1):
    for j in range()