__author__ = 'lyonsmr'

"""
http://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful
instead of subclassing -- create mixins
"""

class FastQIO(object):

    def fastq(self):
        #optimally use some pattern here but for sake of example
        return ">demo\nATGC\n+\nIIII"

class BAMIO(object):

    def bam(self):
        return "QNAME\tFLAG\tRNAME\tPOS\tetc"

class SeqIO(FastQIO, BAMIO):
    #decorate by adding additional tags or something
    pass

if __name__ == '__main__':
    #mixins
    s = SeqIO()
    print s.fastq()
    print s.bam()





