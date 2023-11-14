num=int(input("ENTER NUMBER"))
rem=0
summ=0
while num>0:
    rem=num%10
    summ=summ+rem
    num=num//10
print("SUM OF DIGITS:::",summ)
