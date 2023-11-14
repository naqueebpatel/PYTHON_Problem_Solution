list1=[]
while True:
    num=int(input("ENTER ELEMENTS?"))
    list1.append(num)
    ch=input("MORE ELEMENTS? Y/N")
    if ch=='N':
        break
print("LIST 1:::",list1)
list2=[]
while True:
    num=int(input("ENTER ELEMENTS?"))
    list2.append(num)
    ch=input("MORE ELEMENTS? Y/N")
    if ch=='N':
        break
print("LIST 2:::",list2)
tup1=tuple(list1)
tup2=tuple(list2)
print("TUPLE 1:::",tup1)
print("TUPLE 2:::",tup2)
list3=[]
list3.append(tup1)
list3.append(tup2)
print("NEW LIST:::",list3)
