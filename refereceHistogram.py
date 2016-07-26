import sys
import os
import HTSeq
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

try:
    genebankFileName=sys.argv[1]
    prokkaFileName=sys.argv[2]
except IndexError: 
	print "Invalid input." 
	raise SystemExit

''' Save genes for each file '''

genebankGenes=[]
genebankFile=HTSeq.FastaReader(genebankFileName)
for gene in genebankFile:
    genebankGenes.append(len(gene))

prokkaGenes=[]
prokkaFile=HTSeq.FastaReader(prokkaFileName)
for gene in prokkaFile:
    prokkaGenes.append(len(gene))

''' Plot histograms'''
''''
fig=plt.figure()
genebankPlot = fig.add_subplot(111)
prokkaPlot=fig.add_subplot(212)


genebankPlot.hist(genebankGenes, bins=range(min(genebankGenes), max(genebankGenes) + 200, 200), color='crimson')
prokkaPlot.hist(prokkaGenes, bins=range(min(prokkaGenes), max(prokkaGenes) + 200, 200), color='blue')
genebankPlot.set_title("GeneBank Gene Size Distribution")
prokkaPlot.set_title("PROKKA Gene Size Distribution")
genebankPlot.set_xlabel("Size in Bp")
prokkaPlot.set_xlabel("Size in Bp")
genebankPlot.set_ylabel("Frequency")
prokkaPlot.set_ylabel("Frequency")
prokkaPlot.set_autoscaley_on(False)
prokkaPlot.set_ylim([0,500])
genebankPlot.set_autoscaley_on(False)
genebankPlot.set_ylim([0,500])
plt.show()
'''

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
