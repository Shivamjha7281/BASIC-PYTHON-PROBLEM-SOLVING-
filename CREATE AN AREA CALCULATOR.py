print("-------Area calculator---------")

print(""""Press 1 to get Area of circle=
Press 2 to get Area of triangle=
Press 3 to get Area of rectangle=
Press 4 to get Area of square=""")

choice=int(input("Enter number between 1 to 4="))

if choice==1:
    print("------Area of circle-------")

    radius=float(input("Enter radius of circle="))
    area=3.14*radius*radius
    print("Area of circle=",area)

elif choice==2:
    print("--------Area of triangle-------")

    base=float(input("Enter base of triangle="))
    height=float(input("Enter height of triangle="))
    area=(base*height)/2
    print("Area of triangle=",area)

elif choice==3:
    print("--------Area of rectangle--------")

    length=float(input("Enter length of rectangle="))
    width=float(input("Enter width of rectangle="))
    area=(length*width)
    print("Area of rectangle=",area)

elif choice==4:
    print("--------Area of square-------")

    side=float(input("Enter side of square="))
    area=side*side
    print("Area of square",area)

else:
    print("Invalid choice")
