#Prime numbers=If a number is divided by 1 and itself then it called a prime number
#example:- 2,3,5,7,11.......etc
# 0, 1 and negative integers are not prime numbers

num=int(input("Enter a number="))
if num==1:
     print("It is not a prime number")
elif num==2:
     print("It is a prime number")
if num>1 and 2:
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
