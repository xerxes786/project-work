#fibonnaci series
a=int(input("Enter the terms"))
b=0                                         
c=1                                         
if a<=0:
    print("The requested series needs to be positive")
else:
    print(b)
    print(c)
    for i in range(2,a):
        d= b + c                          
        b=c
        c=d
        print(d)
