n=int(input("enter number : "))
n_1 = 0  
n_2 = 1  
count = 0
if(n<0):
   print("invalid number")  
else:
   print ("The fibonacci sequence of the numbers is:")  
   while count < n:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1  