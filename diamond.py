n=int(input("Enter a number="))
for i in range(n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()    
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print() 