f=open("abc.txt","r")
p=open("xyz.txt","a")
line=f.readline()
while line !="":
    p.write(line)
    line=f.readline()
f.close()
p.close()
f=open("xyz.txt","r")
line=f.read()
print(line)

