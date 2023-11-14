mylist=[]
while True:
    num=int(input("ENTER NUMBER"))
    mylist.append(num)
    ch=input("MORE DETAILS? Y/N")
    if ch=='N':
        break
esum=0
osum=0
for i in range(len(mylist)):
    if mylist[i]%2==0:
        esum=esum+mylist[i]
    else:
        osum=osum+mylist[i]
print("EVEN SUM:::",esum)
print("ODD SUM:::",osum)
