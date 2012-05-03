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


"""
flyweight
    ex:  re-use objects

demo
"""

class Nucleotide(object):
    #imagine this being a more useful class
    def __init__(self, base):
        self.base = base

class DNA(object):
    def __init__(self, dna_str):
        self.nucleotides = {
            'A':Nucleotide('A'),
            'T':Nucleotide('T'),
            'G':Nucleotide('G'),
            'C':Nucleotide('C'),
            }
        for nucleotide in dna_str:
            print self.nucleotides[nucleotide].base

if __name__ == '__main__':
    #mixins
    s = SeqIO()
    print s.fastq()
    print s.bam()

    #dna test
    DNA("CCCC")



