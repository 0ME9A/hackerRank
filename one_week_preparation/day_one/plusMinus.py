# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Input Format
# The first line contains an integer, n, the size of the array.
# The second line contains  space-separated integers that describe arr[n].

# Output Format
# Print the following 3 lines, each to 6 decimals:
# proportion of positive values
# proportion of negative values
# proportion of zeros

# Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

# Sample Output
# 0.500000
# 0.333333
# 0.166667

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
