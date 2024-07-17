lst=[]
n= int (input("n.of values:"))
i=0
while(i<n):
      q=int(input("Enter element:"))
      lst.append(q)
      i=i+1
tup=tuple(lst)
print (tup)
l=[]
r=0
while(r<len(tup)):
      t=int(tup[r])
      d= (t*t)
      l.append(d)
      r=r+1
tup1=tuple(l)
print (tup1)
