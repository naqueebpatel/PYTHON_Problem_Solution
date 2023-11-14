def Fibonacci(int):
    v1=0
    v2=1
    v3=0
    print("FIBONACCI SERIES TILL:::",num)
    print(v1)
    print(v2)
    for i in range(2,num):
        v3=v1+v2
        print(v3)
        v1=v2
        v2=v3
num=int(input("ENTER NUMBER TO FIND FIBONACCI SERIES?"))
Fibonacci(num)
        
