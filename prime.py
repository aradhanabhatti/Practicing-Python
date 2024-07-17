a=int(input("Enter any number:"))
i=2
b=a/2
while(1<i<=b):
     if(a%i==0):
          print ("Composite")
          break
     i=i+1
else:
     print ("Prime")
