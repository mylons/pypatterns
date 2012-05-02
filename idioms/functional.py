__author__ = 'lyonsmr'


"""
list comprehensions
"""

#way you would make a list in other languages
a_list = [1,2,3]
new_list = []

for item in a_list:
    new_list.append(item)

#python way
new_list = [ item for item in a_list ]

#use functions in list comprehensions
def fn(a):
    return True

new_list = [ fn(item) for item in a_list if item > 0 ]



