s=int(input("Please enter your English marks:"))
b=int(input("Please enter your Maths marks:"))
c=int(input("Please enter your  Science marks:"))
d=s+b+c
a=d/3
print ("Average:",a)
if(a>100 or a<0):
     print ("Marks are invalid")
elif(a>=0 and a<=33):
     print ("fail")
elif(a>33 and a<=45):
     print ("Grade E")
elif(a>45 and a<=60):
     print ("Grade D")
elif(a>60 and a<=75):
     print ("Grade C")
elif(a>75 and a<=85):
     print ("Grade B")
elif(a>85 and a<=95):
     print ("Grade A")
elif(a>95 and a<=100):
     print ("Distinction")

