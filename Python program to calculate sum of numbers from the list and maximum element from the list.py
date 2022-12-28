from functools import reduce
a = [1,2,3,8,9,10,4,5,6,7]
sum = reduce(lambda x,y: x+y,a)
max = reduce(max,a)
print("sum of all the list elements is {0}".format(sum))
print("maximum number in the list is {0}".format(max))
