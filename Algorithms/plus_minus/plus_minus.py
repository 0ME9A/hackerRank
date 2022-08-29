
arr = [-4, 3, -9, 0, 4, 1]
# arr = [7]


def PlusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    
    for i in arr:
        if type(i) == int:
            if i< 0:
                negative +=1
            if i> 0:
                positive +=1
            if i == 0:
                zeros += 1

    posDivide = positive/len(arr)
    negDivide = negative/len(arr)
    zeeDivide = zeros/len(arr)

    print(format(posDivide, '.6f'))
    print(format(negDivide, '.6f'))
    print(format(zeeDivide, '.6f'))
    # return "%s\n%s\n%s"%(posFloat, negFloat, zeeFloat)


PlusMinus(arr)
