x=int(input("how many:"))
lst=[]
i=0
while(i<x):
      a=int(input("1st"))
      lst.append(a)
      i=i+1

lst.sort(reverse=True)
print (lst)
