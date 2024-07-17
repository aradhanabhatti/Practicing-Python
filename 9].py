l=int(input("enter total no of elemets:"))
q=[]
i=0
while(i<l):
     a=int(input("Enter element:")) 
     q.append(a)
     i=i+1
print (q)

s=0
m=0
while(s<len(q)):
     m=m+q[s]
     s=s+1
print (m)
