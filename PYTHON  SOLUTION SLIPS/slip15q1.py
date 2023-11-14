mytup=()
while True:
    num=int(input("ENTER ELEMENT?"))
    mytup=mytup+(num,)
    ch=input("MORE ELEMENTS? Y/N")
    if ch=='N':
        break;
print(mytup)
x=int(input("ENTER NUMBER TO CHECK"))
if x in mytup:
    print(x," IS PRESENT")
else:
    print(x," IS NOT PRESENT")
