mylist=[]
while True:
    num=int(input("ENTER ELEMENT"))
    mylist.append(num)
    ch=input("MORE ELEMENTS? Y/N")
    if ch=='N':
        break
print("ORIGINAL LIST:::",mylist)
myset=set(mylist)
mylist=list(myset)
print("DUPLICATES REMOVED LIST:::",mylist)
