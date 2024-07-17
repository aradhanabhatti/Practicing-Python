a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
even=0
odd=0
i=a
while(i<=b):
     if(i%2==0):
          even=even+i
     else:
          odd=odd+i
     i=i+1
print ("Sum of even numbers:",even)
print ("Sum of odd numbers:",odd)
