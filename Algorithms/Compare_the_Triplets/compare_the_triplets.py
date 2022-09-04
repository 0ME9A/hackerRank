# Compare-the-Triplets

def CompareTheTriplets(a, b):
    aliceInitialPoint = 0
    bobInitialPoint = 0
    if len(a) == len(b):
        i = 0
        while i<len(a):
            if a[i] > b[i]:
                aliceInitialPoint+=1
            if a[i] < b[i]:
                bobInitialPoint+=1
            i=i+1
    else:
        print ('Data are Not same')

    print (aliceInitialPoint)
    print (bobInitialPoint)
    # return (aliceInitialPoint, bobInitialPoint)


alice = [3,4,99]
bob = [33,32,22]

CompareTheTriplets(alice, bob)