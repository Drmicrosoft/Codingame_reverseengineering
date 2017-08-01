def omar (y):

	print 'omar'
	print y


filename = "1"
file = open(filename, "r")
x=""
for line in file:
   x=x+line
print x + "omar"


g=0
i=0
ln = [0,0,0,0,0,0,0]
while (i<6) :
	g = x.find("-",g)
	print g
	ln[i]=g
	print x[g:g+1]
	g=g+2
	i=i+1


print ln
omar1=x
j=0

while j < 5 :
	x=omar1[ln[j]:ln[j+1]]
	
	print "start ************** " , x[ln[j]:ln[j]+100]
	y=0
	o=0
	while 1 :
		print "Lets start from  " , ln[j] , " to " , ln[j+1] , " this is number = " , y
		y=y+1
		o = x.find("firstInput",o)
		print o
		k = input("reading")

		print "Lets start 1"
		if(o==-1):
			k = input("omarrrrr")
			break
		o=o+len("firstInput")
		o3 = x[o:o+1]
		print o , o3

		o = x.find("secondInput",o)
		o=o+len("secondInput")
		o3 = x[o:o+1]
		print o , o3


		o = x.find("thirdInput",o)
		o=o+len("thirdInput")
		o3 = x[o:o+1]
		print o , o3


		o = x.find("fourthInput",o)
		o=o+len("fourthInput")
		o3 = x[o:o+1]
		print o , o3

		i=0
		while (i<5) :
			o = x.find("fifthInput",o)
			o1 = x.find("'",o)
			o2 = x.find("'",o1+1)
			o3 = x[o1+1:o2]
			print o , o1 ,o2 , o3

			o = x.find("sixthInput",o)
			o1 = x.find("'",o)
			o2 = x.find("'",o1+1)
			o3 = x[o1+1:o2]
			print o , o1 ,o2 , o3
			i=i+1
	j=j+1



k = input("omarrrrr")
print "\n\n\n\n\n\n\n\n"
o = x.find("firstInput",o)
o=o+len("firstInput")
o3 = x[o:o+1]
print o , o3

o = x.find("secondInput",o)
o=o+len("secondInput")
o3 = x[o:o+1]
print o , o3


o = x.find("thirdInput",o)
o=o+len("thirdInput")
o3 = x[o:o+1]
print o , o3


o = x.find("fourthInput",o)
o=o+len("fourthInput")
o3 = x[o:o+1]
print o , o3


o = x.find("fifthInput",o)
o1 = x.find("'",o)
o2 = x.find("'",o1+1)
o3 = x[o1+1:o2]
print o , o1 ,o2 , o3

o = x.find("sixthInput",o)
o1 = x.find("'",o)
o2 = x.find("'",o1+1)
o3 = x[o1+1:o2]
print o , o1 ,o2 , o3



print x[o+14:o+15]
print "end"




