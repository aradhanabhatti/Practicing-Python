lst=[]
a=int(input("Enter total subjects:"))
i=0
while(i<a):
     q=int(input("Please enter marks:"))
     lst.append(q)
     i=i+1
print (lst)

s=0
m=0
while(s<len(lst)):
     m=m+lst[s]
     s=s+1
print (m)










