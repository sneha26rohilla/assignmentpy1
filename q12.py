n=int(input("enter a number : "))
sum=0
while(n>0):
    i=int(n%10)
    n=int(n/10)
    sum=sum+i
print("the sum of digits is ",sum)