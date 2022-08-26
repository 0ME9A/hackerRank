# A Very Big Sum


def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for i in ar:
        if type(i) == int:
            sum=sum+i
    print (sum)
    return sum


sumThis = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

aVeryBigSum(sumThis)