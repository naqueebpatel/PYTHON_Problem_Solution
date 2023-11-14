def RemoveOdd(str):
    st=" "
    for i in range(len(mystr)):
        if i%2==0:
            st=st+mystr[i]
    print(st)
mystr=input("ENTER STRING")
RemoveOdd(mystr)
