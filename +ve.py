a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
s=0
y=0
i=a
while(i<=b):
     if(i>0):
          s=s+1
     if(i<0):
          y=y+1
     if(i==0):
          print ("Zero exists")
     i=i+1
print ("positive nos:",s)
print ("negative nos:",y)


