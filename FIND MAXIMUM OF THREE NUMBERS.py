def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the greatest number")
    elif val2>val3 and val2>val1:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")
maximum_num(21,22,23)