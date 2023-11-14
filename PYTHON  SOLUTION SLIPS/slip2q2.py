def CountString():
    mydict={}
    mystr=input("ENTER STRING?")
    for i in mystr:
        if i in mydict:        
            mydict[i]+=1
        else:
            mydict[i]=1
    print(mydict)
CountString()
