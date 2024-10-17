def my_range(start, stop, step=1):
    result=[]
    current = start
    while current<stop:
        result.append(current)
        current+=step
    return result
    
def my_enumerate(iterable, start=0):

    return list(enumerate(iterable))

def my_enumerate2(iterable2, start=0):
    result2 = []
    index=0
    for value in iterable2:
        result2.append(index, value)
        index += 1
    return result2

def while_enumerate(iterable3, start=0):
    result3= []
    i=0
    while i< len(iterable3):
        result3.append((i+start, iterable3[i]))
        i+=1
    return result3

def my_zip(*iterables):
    results = []
    lenght = len(iterables[0])
    for i in range(0,lenght):
        subresult=[]
        for j in range(0,len(iterables)):
            subresult.append(iterables[j][i])
        results.append(tuple(subresult))
        print (i, iterables[1][i])

    return results


if __name__=="__main__":
    #print(list(range(1,10,2)))
    #print(my_range(1,10,2))

    print(list(enumerate("abcdef")))
    print(my_enumerate("abcdef"))

    print(list(enumerate(["Alice", "Bob", "Eva"])))
    print(my_enumerate(["Alice", "Bob", "Eva"]))

    print (list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a","b","c"])))
    print (my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12], ["a","b","c"]))
    