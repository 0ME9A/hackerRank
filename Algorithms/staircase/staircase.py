# 8Staircase detail


def stair(n):
    if type(n) == int or type(n) == float:
        symbol1 = ' '
        symbol2 = '#'

        for i in range(n):
            print ((symbol1*(n - (i+1))) + (symbol2 * (i+1)))

    else:
        print ('invalid input.')


getInput = int(input("Give a number:- "))
stair(getInput)