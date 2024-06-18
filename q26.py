
a=input("enter text : ")
b=input("enter suffix/prefix to remove : ")

c=a.removeprefix(b)
d=a.removesuffix(b)

print("string without prefix " , c)
print("string without suffix " , d)