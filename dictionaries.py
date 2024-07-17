days={"Jan":31,"feb":28,"march":31,"april":30}
for key in days:
      print (days[key])


lst=[21,54,67,54,21,98,0,0,90]
dic={}
for item in lst:
      key=item
      if key not in dic:
            dic[key]=lst.count(item)
print ("Counting frequencies in list", dic)
