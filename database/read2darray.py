z=[]
dat=open("/home/jonesy/projects/BelajarPyton/database/data.txt","r+")
line = dat.read()

line=line.split(";\n")

for l in line:
	l=l.split(",")
	z.append(l)
 
print(z) 
dat.close()
