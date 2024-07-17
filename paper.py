lst=[21,65,32,32,14,5,21,8,]
dic={}
for item in lst:
      key=item
      if key not in dic:
            dic[key]=lst.count(item)
print (dic)
