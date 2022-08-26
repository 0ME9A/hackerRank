// A Very Big Sum


function aVeryBigSum(ar) {
    // Write your code here
    let sum = 0
    for (let i = 0; i < ar.length; i++) {
        const element = ar[i]
        if (typeof element  == "number"){
            sum = sum + element
        }
    }
    console.log(sum)
    return sum
}


const sumThis = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

aVeryBigSum(sumThis)