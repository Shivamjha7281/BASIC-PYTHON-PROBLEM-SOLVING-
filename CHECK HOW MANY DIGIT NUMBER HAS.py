number=int(input("Enter number here upto 5 digits="))
if number>=0 and number<=9:
    print("It is a single digit number")
elif number>=10 and number<=99:
    print("It is double digit number")
elif number>=100 and number<=999:
    print("It is three digit number")
elif number>=1000 and number<=9999:
    print("It is four digit number")
elif number>=10000 and number<=99999:
    print("It is five digit number")
else:
    print("I can only tell you about till five digit"
          "numbers")