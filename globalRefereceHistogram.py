import sys
import os
import HTSeq
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

try:
    genebankFileDir=sys.argv[1]
    prokkaFileDir=sys.argv[2]
except IndexError: 
	print "Invalid input." 
	raise SystemExit


''' Save genes for each file '''
os.chdir(genebankFileDir)
genebankGenes=[]
l=os.listdir(genebankFileDir) 
for fastaFiles in l:
	genebankFile=HTSeq.FastaReader(fastaFiles)
	for gene in genebankFile:
		genebankGenes.append(len(gene))

os.chdir(prokkaFileDir)
prokkaGenes=[]
l=os.listdir(prokkaFileDir) 
for fastaFiles in l:
	prokkaFile=HTSeq.FastaReader(fastaFiles)
	for gene in prokkaFile:
		prokkaGenes.append(len(gene))

''' Plot histograms'''

print 'PROKKA Genes: %s' % len(prokkaGenes)
print 'GeneBank Genes: %s' % len(genebankGenes)

plt.hist(prokkaGenes, bins=range(min(genebankGenes), max(genebankGenes) + 200, 200), color='blue', alpha=0.6,label='PROKKA')
plt.hist(genebankGenes, bins=range(min(genebankGenes), max(genebankGenes) + 200, 200), color='red', alpha=0.5,label='GeneBank')
plt.xlabel("Size in Bp")
plt.ylabel("Frequency")
plt.title("Gene Size Distribution")
plt.grid(True)
plt.legend()
plt.show()