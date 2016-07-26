import sys
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

try:
	SDSEfilesDirectory=sys.argv[1] 
	#outputDirectory=sys.argv[2] 
except IndexError: 
	print "Invalid input." 
	raise SystemExit

os.chdir(SDSEfilesDirectory)
l=os.listdir(SDSEfilesDirectory)

d={}

for item in l:
	SDSEfile = open(item, 'r')
	for line in SDSEfile:
		if not line.startswith('>'):
			d[item]=len(line)

values=[]
for key, value in d.iteritems():
	values.append(value)


#Making the plot 

plt.hist(values, bins=range(min(values), max(values) + 200, 200), color='crimson')
plt.xticks(np.arange(min(values), max(values)+1, 200), rotation=90)
plt.title("Gene Size Distribution")
plt.xlabel("Size in Bp")
plt.ylabel("Frequency")
plt.show()

