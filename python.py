a=int(input("Enter number of rows"))
b=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(b,end=" ")
        b+=1
    print()