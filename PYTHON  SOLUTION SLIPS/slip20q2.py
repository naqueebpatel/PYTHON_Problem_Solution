num=int(input("ENTER NO OF ROWS?"))
x=1
for i in range(num):
    for j in range(i+1):
        print(x,end=" ")
        x+=1
    print("\n")
