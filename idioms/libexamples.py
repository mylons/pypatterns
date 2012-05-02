__author__ = 'lyonsmr'

#plot several series
import matplotlib.pyplot as pyplot

def plot_list(xs, ys, clf=False, label=None):
    if clf:
        pyplot.clf()
    line = pyplot.plot(xs, ps, label=name)

def make_plots(lists_of_x, lists_of_y):
    #assumes they're equal length lists of lists [ [ ] ]
    for i in xrange(lists_of_x):
        plot_list(lists_of_x[i], lists_of_y[i], label=i, clf=False)


#pysam examples
import pysam

""" get aligned reads to a specific region"""
#rb stands for read, binary
samfile = pysam.Samfile("something.bam", "rb")
for alignedread in samfile.fetch("chr1", 100, 120):
    print alignedread
samfile.close()

""" pileup """
for pileupcolumn in samfile.pileup( "chr1", 100, 120 ):
    print 'coverage at base %s = %s' % ( pileupcolumn.pos, pileupcolumn.n )
    for pileupread in pileupcolumn.pileups:
        print '\tbase in read %s = %s' % ( pileupread.alignment.qname, pileupread.alignment.seq[ pileupread.qpos ] )



