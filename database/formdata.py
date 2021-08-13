dat=open("/home/jonesy/projects/BelajarPyton/database/data.txt","r+")
line = dat.read()

i=0

for r in line:
    for c in r:
        print(c,end=" ")

print ("Read Line: %s" % (line))
dat.close()