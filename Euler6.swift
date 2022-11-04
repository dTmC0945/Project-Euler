func sumOfSquares(n: Int) -> Int {                      // function that calculates the sum of squares up to number n

    var cache = 0
    var square = 0
    var i = 0

    while (i <= n) {
        square = i * i
        cache = square + cache
        i += 1
    }

    return cache
}

func squareOfSums(n: Int) -> Int {                     // function that calculates the square of sums up to number n

    var cache = 0
    var sum = 0
    var i = 0

    while (i <= n) {
        sum = i
        cache = sum + cache
        i += 1
    }

    return cache * cache
}

let numA = sumOfSquares(n: 100)

let numB = squareOfSums(n: 100)

print(numB - numA)                                      // finds the differece