import sys
#import prolog

print
print "Starting Program ..."
print
try:
	print "trying to open geoQuery880.xml\n"	
	f=open("geoquery880.xml","r")
except e:
	print "Unable to open file"
	print
	sys.exit(1)
	
file=f.read()
f.close()
#print 
#print 
#print file
#print 
#print
#sys.exit(1)
start=end=0
index=1
q=[]
geoQueryDB_list={}
while(index<881):
	print "\nwhile%d" % index
	pos=file.find("<example id=")
	pos=file.find("<nl lang=\"en\">",pos)
	pos=pos+14
	start=pos
	pos=file.find("</nl>",start)
	end=pos
	x=file[start:end]
	x=x.strip()
	print
	print x
	print
	file=file[end:]
	#if index>878:
	#	print
	#	print file
	#	print
	pos=file.find("<mrl lang=\"geo-funql\">")
	pos=pos+22
	start=pos
	pos=file.find("</mrl>",start)
	end=pos
	z=file[start:end]
	z=z.strip()
	print
	print z
	print
	file=file[end:]
	#if index>878:
	#	print
	#	print file
	#	print
	q=[x,z]
	geoQueryDB_list[index]=q
	index=index+1
	
try:
	print "trying to open geoQuery880_DB.txt\n"
	f=open("geoQuery880_DB.txt","wb")
	
except e:
	print "unable to open file"
	print
	sys.exit(1)
	
n=sorted(geoQueryDB_list.keys())

for i in n:
	q=geoQueryDB_list[i]
	x=q[0]
	x=str(x)
	z=q[1]
	z=str(z)
	data="\n%d\nQuery(x)     :     %s\nMR(z)        :     %s\n" % (i,x,z)
	f.write(data)

f.close()

try:
	print "trying to open Response250(training).txt\n"
	f=open("Response250(training).txt","wb")
	
except e:
	print "unable to open file"
	print
	sys.exit(1)

	
i=0
while(n[i]<251):
	q=geoQueryDB_list[n[i]]
	x=q[0]
	x=str(x)
	z=q[1]
	z=str(z)
	#r=execute(z)
	r="r%d" % (i+1)
	data="\n%d\nQuery(x)     :     %s\nResult(r)    :     %s\n" % ((i+1),x,r)
	f.write(data)
	i=i+1
	
f.close()
	
	
try:
	print "trying to open Query250(test).txt\n"
	f=open("Query250(test).txt","wb")
	
except e:
	print "unable to open file"
	print
	sys.exit(1)

	
i=250
j=1
while(n[i]<501):
	q=geoQueryDB_list[n[i]]
	x=q[0]
	x=str(x)
	data="\n%d\nQuery(x)     :     %s\n" % (j,x)
	f.write(data)
	i=i+1
	j=j+1
	
f.close()

print "\nExiting Program\n\n"

	
	
	