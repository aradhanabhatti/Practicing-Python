w=float(input("Enter weight in kg:"))
h=float(input("Enter height in m:"))
height=h*h
b=w/height
print ("BMI:",b)
if(b>0 and b<18):
      print ("Undernourished")
elif(b>18 and b<25):
      print ("Normal")
elif(b>25 and b<33):
      print ("Overweight")
elif(b>33):
      print ("Obese")
