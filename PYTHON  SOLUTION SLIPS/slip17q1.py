mydict={}
while True:
    key=int(input("ENTER KEY"))
    value=input("ENTER VALUE")
    mydict[key]=value
    ch=input("MORE DETAILS? Y/N")
    if ch=='N':
        break
print("DICTIONARY:::",mydict)
check=int(input("ENTER KEY TO CHECK WHETHER EXIST'S OR NOT?"))
if check in mydict.keys():
    print("KEY IS PRESENT")
    nkey=int(input("ENTER KEY TO UPDATE?"))
    nval=input("ENTER VALUE TO UPDATE?")
    mydict[nkey]=nval
    print("UPDATED DICTIONARY:::",mydict)
else:
    print("KEY DOES NOT EXIST")
