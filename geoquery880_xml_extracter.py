import sys

try:
	
	f=open("geoquery880.xml","r")
except e:
	print "Unable to open file"
	sys.exit(1)
	
file=f.read()
line=0
while(!file):
	
	pos=file.find("<example id=\"66\">")
	pos=file.find("<nl lang=\"en\">",pos)
	pos=pos+14
	start=pos
	pos=file.find("</nl>",start)
	end=pos
	x=file[start:end]
	x=x.strip()
	file=file[end:]
	pos=file.find("<mrl lang=\"geo-funql\">")
	pos=pos+22
	start=pos
	pos=file.find("</mrl>",start)
	end=pos
	z=file[start:end]
	file=file[end:]