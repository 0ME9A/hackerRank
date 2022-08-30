# birthday_cake_candles


def birthdayCakeCandles(candles):
    maxNum = max(candles)
    moreThen = 0
    for i in candles:
        if type(i) == int and maxNum == i:
            moreThen+=1
    print (moreThen)
        

arr = [3, 2, 1, 3]
birthdayCakeCandles(arr)