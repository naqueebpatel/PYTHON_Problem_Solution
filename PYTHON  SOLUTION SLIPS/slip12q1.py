mylist=[]
while True:
    num=int(input("ENTER NUMBER"))
    mylist.append(num)
    ch=input("MORE ELEMENTS? Y/N")
    if ch=='N':
        break
print(mylist)
mx=mylist[0]
mn=mylist[0]
for i in range(len(mylist)):
    if(mylist[i]>mx):
        mx=mylist[i]
    if(mylist[i]<mn):
        mn=mylist[i]
print("MAX:::",mx)
print("MIN:::",mn)
