list1=[]
for i in range(10):
    num=int(input("ENTER ELEMENT"))
    list1.append(num)
set1=set(list1)
if(len(set1)==len(list1)):
    print("ALL UNIQUE");
else:
    print("DUPLICATES PRESENT")
print(list1)
