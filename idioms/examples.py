__author__ = 'lyonsmr'


#white space is everything
####4 spaces is standard indent.
#don't mix spaces and tabs for indents

#boolean values True and False
a = True
b = False
if a == b:
    print "a == b"
elif a != b:
    print "a != b"
else:
    print "this shouldn't happen, but this is a common if, else if, and else block"

#example:
if True:
    #do this
    print "hi"

#how to hash
d = {}
value = 4
d['key'] = value

#test if it's in there
if 'key' in d:
    print d['key']


#open file and loop throuhg it
#write to an output file too
f = open("/tmp/this_file_better_be_there.txt", "w")
f.write("blah\n")
f.close()

f = open("/tmp/this_file_better_be_there.txt", "r")
for line in f:
    print line

#traditional for loop in python:
#for (int i = 0; i < 40; i++) -- C equiv
for i in xrange(40):
    #prints 0-39 on new lines
    print i


while True:
    #do w/e we have here
    if True:
        #break from a loop
        break
    else:
        #continue a loop
        continue



"""
functions in python
"""

def add_params(param1, param2):
    #param1 and param2 are some type of variable passed to
    #this function
    return param1 + param2

#example call
add_params(1, 2)

#when calling this function, you do not have to specify param2
def add_params2(param1, param2=2):
    return param1 + param2

#example call
add_params2(1, param2=9)
#or
add_params2(1, 2)


