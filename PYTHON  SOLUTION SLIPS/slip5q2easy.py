tup1=()
while True:
    num=int(input("ENTER NUMBER"))
    tup1=tup1+(num,)
    ch=input("MORE ENTERIES? Y/N")
    if ch=='N':
        break
print(tup1)
print(tup1[:len(tup1)//2])
print(tup1[len(tup1)//2:])
