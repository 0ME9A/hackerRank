// Compare-the-Triplets

CompareTheTriplets=(a, b)=>{
    aliceInitialPoint = 0
    bobInitialPoint = 0

    if (a.length === b.length) {
        for (let i = 0; i < a.length; i++) {
            const element = a[i];
            if (a[i] > b[i]) {
                aliceInitialPoint++
            }
            if (a[i] < b[i]){
                bobInitialPoint++
            }
        }
    }
    else{
        console.log('Data are not same')
    }

    console.log(aliceInitialPoint, bobInitialPoint)
    // return (aliceInitialPoint, bobInitialPoint)
}


const alice = [17, 28, 30]
const bob = [99, 16, 8]

CompareTheTriplets(alice, bob)