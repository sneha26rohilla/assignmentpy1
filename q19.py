import string

a=input("enter text : ")
c=list(string.punctuation)

b=list(a)
for i in b:
    for p in c:
       if(i==p):
           b.remove(i)
           print(b)

print("string without punctuation is " , str(b))

