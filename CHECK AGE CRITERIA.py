y=int(input("Enter your age="))
if(y>0 and y<=13):
    print("kid")
elif(y>13 and y<=19):
    print("teenager")
elif(y>19 and y<=30):
    print("young")
elif(y>30 and y<=45):
    print("mature")
elif(y>45 and y<=60):
    print("experienced")
elif(y>60 and y<=75):
    print("old")
elif(y>75):
    print("senior citizen")