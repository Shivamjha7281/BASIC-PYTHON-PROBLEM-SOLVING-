a=int(input("enter a number="))
factorial=1
if a<0:
    print("sorry, factorial does not exist for negative number")
elif a==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print("factorial of",a,"is",factorial)