a=float(input("Enter first number="))
b=float(input("Enter second number="))
c=float(input("Enter third number="))
d=float(input("Enter fourth number="))
if(a>b and a>c and a>d):
    print("Greatest number is=",a)
elif(b>c and b>d):
    print("Greatest number is=",b)
elif(c>d):
    print("Greatest number is=",c)
elif(d>c):
    print("Greatest number is=",d)
else:
    print("Either two or all four values are equal")
