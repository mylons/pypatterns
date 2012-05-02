__author__ = 'lyonsmr'
import pprint


#regular expressions

import re
cigar = "32M1I89M1D7M1D37M1D16M1I71M1I12M1I18M1I19M3S"
matches = re.findall("([0-9]+)([A-Z]+)", cigar)
for length, operation in matches:
    print operation, length


#don't do this.  creates a lot of string objects (same is true for any language)
def join_strings_bad(list_of_strings):
    result = ''
    for s in list_of_strings:
        result += ' ' + s

#best practice to join strings by a single space
def join_strings(list_of_strings):
    return ' '.join(list_of_strings)


#iterate throuhg keys of a dictionary
d = {}

#if you don't add or remove from teh dictionary this is ok
for key in d:
    #print's hash key
    print key
    #print value
    print d[key]

"""
if you do want to change the dictionary you must generate the keys
in an iterable form first that is outside the scope of the dictionary
"""
for key in d.keys():
    #this is adding a new key to the dictionary
    d[str(key)+"suffixtokey"] = d[key]

"""
make a dict out of 2 lists and prints the dictionary
{'John': 'Cleese',
 'Michael': 'Palin',
 'Eric': 'Idle',
 'Terry': 'Gilliam'}
"""

given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']
pythons = dict(zip(given, family))


"""
want to iterate a list and keep track of the index of the value you're at?
"""
for (index, name) in enumerate(given):
    #enumerate is a function that returns 2 values at the same time.
    #called a tuple
    print index, name



"""
basic exception handling
"""

try:
    this_will_raise_an_exception = pythons['Mike']
except KeyError:
    print "Mike isn't a member of Monty Python"



"""
default parameter values
"""

def i_have_a_default(a, b=1, c=True, d="string"):
    print a,b,c,d

i_have_a_default(1, b=3, d="hello", c="neat?")



"""
a simple class
"""


class Simple(object):
    #the class declaration means Simple inherits from object -- which is the base object type in python

    #class constructor for python
    def __init__(self):
        """
            in order to create member variables you need
            to prefix their names with self.
            you also call functions, from within a class,
            with self.function_name()
        """
        self.a = 4

    def a(self):
        return self.a



#make a new Simple instance
testSimple = Simple()
#statement below should print 4
print testSimple.a

