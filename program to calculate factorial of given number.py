from functools import reduce
n = int(input("enter the number:- "))
fact = reduce(lambda x,y:x*y,range(1,n+1))
print(fact)
