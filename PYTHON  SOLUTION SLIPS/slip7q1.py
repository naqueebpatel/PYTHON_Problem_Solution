num=int(input("ENTER NUMBER"))
print("PRIME NUMBERS ARE:::")
for i in range(2,num+1):
    cnt=0
    for j in range(1,i+1):
        if(i%j==0):
            cnt+=1
    if(cnt==2):
        print(i)
    
