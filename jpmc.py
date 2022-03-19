res="Hello\nworld\nis \ntapioca"

newstr=res.split("\n")
#print(newstr)

newres=""
for x in newstr:
    newres+=x.strip().capitalize()+" "
    
print(newres)    