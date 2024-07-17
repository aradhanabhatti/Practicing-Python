d1={1:40,2:70,3:70}
d2={1:40,2:50,3:60}
d3={1:70,2:80,3:90}
d4={"Suniti":d1,"Ryna":d2,"Zeba":d3}
for x in d4.keys():
      print ("Name")
      print (x)
      print ("subject(key)", "marks(value)")
      for  y in d4[x].keys():
            print (" ",y, d4[x][y])
            print ()
