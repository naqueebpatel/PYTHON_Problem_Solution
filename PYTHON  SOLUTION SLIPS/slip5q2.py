tup1=()
while True:
    num=int(input("ENTER NUMBER"))
    tup1=tup1+(num,)
    ch=input("MORE ENTERIES? Y/N")
    if ch=='N':
        break
print("TUPLE ELEMENTS:::",tup1)
for i in range(len(tup1)):
        if i<len(tup1)//2:
            print(tup1[i],end=" ")
print()
for i in range(len(tup1)//2,len(tup1)):
    if i>=len(tup1)//2:
        print(tup1[i],end=" ")
