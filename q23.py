a=(input("enter temperature : "))
if(a[-1]=="C"):
    b=int(a[:-1])
    print("temp in Fahrenheit",(9/5)*b + 32)
if(a[-1]=="F"):
    p=int(a[:-1])
    print("temp in Celsius",(p-32)*5/9)


    