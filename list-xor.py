def listXor(target, listOne, listTwo):
    finished = False
    while(finished==False):
        if(len(listOne)!=(len(listTwo))):
            finished = True
            return False
        for x in range(len(listOne)):
            if(listOne[x]==target or listTwo[x]==target):
                if(listOne[x]==target and listTwo[x]!=target):
                    return "In list one"
                elif(listOne[x]!=target and listTwo[x]==target):
                    return "In list two"
                else:
                    return "error"
        return "Not in either list"
        finished = True



arrOne = [1,2,3]
arrTwo = [4,5,6]
target = 7
print(listXor(target, arrOne, arrTwo))