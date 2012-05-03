__author__ = 'lyonsmr'

""" Singleton Examples"""
class Singleton:
    __single = None

#one way
class Singleton1(Singleton):
    def __init__( self ):
        if Singleton.__single:
            raise Singleton.__single
        #this line of code is never reached
        #if __single already exists
        Singleton.__single = self

#another way
class Singleton2(Singleton):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '__instance__'):
            orig = super(Singleton2, cls)
            cls.__single = orig.__new__(cls, *args, **kw)
        return cls.__single


class SingletonDemo(Singleton1):
    a = 1

def singleton_demo():
    """Singleton demo"""
    one = SingletonDemo()
    two = SingletonDemo()
    two.a = 4
    #one.a should now be 4 as well
    print one.a


""" adapter examples """
class FastQAdapter(object):
    def __init__(self, fastq_record):
        self._fastq_tokens = fastq_record.split('\n')
        self._name = fastq_tokens[0]
        self._dna = fastq_tokens[1]
    def dna(self):
        return self._dna
    def name(self):
        return self._name

class DNASeq(object):
    def summary(self, fastq_adapter):
        print 'Name: %s\nDNA=%s' % (fastq_adapter.name(), fastq_adapter.dna())

def adapter_demo():
    fastq = FastQAdapter("@bead_id\nATGCATGC\n+\nIIIIIIII")
    dna = DNASeq()
    dna.summary(fastq)


"""
    builder example
"""

class BEDLine(object):
    def __init__(self, builder):
        self._ref = builder._ref
        self._start_pos = builder._start_pos
        self._stop_pos = builder._stop_pos
        #optional fields default values
        self._name = builder._name
        self._score = builder._score
        self._strand = ""#legal values are + -
        self._unique_id = builder._unique_id
        self._final_tag = builder._final_tag
    def __str__(self):
        ret_str = "%s\t%s\t%s" % (
            self._ref,
            str(self._start_pos),
            str(self._stop_pos)
            )
        def append_str(s):
            #inefficient
            if (s):
                ret_str = "%s\t%s" % (ret_str, s)
        append_str(self._name)
        append_str(self._score)
        append_str(self._strand)
        append_str(self._unique_id)
        append_str(self._final_tag)
        return ret_str


    class Builder(object):
        delim = "\t"
        def __init__(self, reference_id="", start_position="", stop_position=""):
            #mandatory fields
            self._ref = reference_id
            self._start_pos = start_position
            self._stop_pos = stop_position
            #optional fields default values
            self._name = ""
            self._score = ""
            self._strand = ""#legal values are + -
            self._unique_id = ""
            self._final_tag = []

        def ref(self, ref):
            self._ref = ref
            return self
        def start_pos(self, start_pos):
            self._start_pos = start_pos
            return self
        def stop_pos(self, stop_pos):
            self._stop_pos = stop_pos
            return self
        def name(self, name):
            self._name = name
            return self
        def score(self, score):
            self._score = score
            return self
        def strand(self, strand):
            self._strand = strand
            return self
        def unique_id(self, unique_id):
            self._name = unique_id
            return self
        def final_tag(self, final_tag):
            self._final_tag.append(final_tag)
            return self
        def build(self):
            self._final_tag = self.delim.join(self._final_tag)
            return BEDLine(self)

class BEDFile(object):
    #sort of overkill and redundant but an example none the less
    class LineAdapter(object):
        def __init__(self, line):
            self.tokens = line.strip('\r\n').split('\t')
        def ref(self):
            return self.tokens[0]
        def start(self):
            return self.tokens[1]
        def stop(self):
            return self.tokens[2]


    def __init__(self, filename):
        self._filename = filename
        try:
            self._fp = open(filename, "r")
        except:
            #TODO change this to a logger
            print "Cannot open file %s " %  filename

    def bedlines(self):
        for line in self._fp:
            adpt = BEDFile.LineAdapter(line)
            yield BEDLine.Builder().ref( adpt.ref() ).start_pos( adpt.start() ).stop_pos( adpt.stop() ).build()

    def __exit__(self, type, value, traceback):
        try:
            self._filename.close()
        except:
            #we don't care if an exception is thrown
            pass

if __name__ == '__main__':
    print "hi"

