
def addList(array1,array2):
    res = list(map(lambda x,y:x+y,array1,array2))
    return res
def subList(array1,array2):
    res = list(map(lambda x,y:x-y,array1,array2))
    return res
array1 = [5,4,3,1,3,7,8,10]
array2 = [4,2,1,0,9,8,4,1]

print(addList(array1,array2))
print(subList(array1,array2))
