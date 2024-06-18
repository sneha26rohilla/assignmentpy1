a=int(input("enter num1 "))
n=a
p=a
b=1
for i in range(a):
    b=b*i
print("factorial is ", b)

while(a>0):
    n=(a-1)*(a)
    print(n)
    a=a-2
    
print("factorial of ",p," is ",n)