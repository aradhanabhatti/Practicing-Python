
lst=[]
n=int(input("enter no."))
i=0
while(i<n):
     b=input("enter elements:")
     lst.append(b)
     i=i+1
tup=tuple(lst)
r=0
while(r<len(tup)):
     t=int(tup[r])
     print (t*t)
     r=r+1
