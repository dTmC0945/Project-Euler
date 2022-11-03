func collatzChain(n: Int) -> Int {                      // First function actually creates the collatz chain for the
                                                        // entered number starting counting from the entered number
    var number = n                                      // all the way to number 1.
    var collatzArray: [Int] = [n]

    while (number != 1) {
        if (number % 2 == 0) {
            number = Int(Double(number / 2))
            collatzArray.append(number)
        } else {
            number = number * 3 + 1
            collatzArray.append(number)
        }
    }

    return collatzArray.count                           // this function returns the size of the chain.
}

func collatzSize(m: Int) -> Array<Int> {                // this function lists the size of collatz chain up to the limit
                                                        // given by the question (in this case it is 1,000,000
    var value = 1
    var size: [Int] = []
    var iter = 0

    while (value < m) {
        size.append(collatzChain(n: value))
        value += 1
        iter += 1
    }

    return size                                         // this function returns an array of chain sizes with a length
}                                                       // equal to entered numbers

func maxFinder(p: Int) -> Int {                         // final function finds the maximum chain length and the number
                                                        // it is associated with.
    var UpperLimit = p
    let Array = collatzSize(m:UpperLimit)
    var maxValue = Array[0]
    var maxIndice = 0
    var indice = 0

    while(indice < Array.count) {
        if (maxValue < Array[indice]){
            maxValue = Array[indice]
            maxIndice = indice + 1
        }
        indice += 1

    }
    print("Highest collatz Chain under \(UpperLimit) is the number \(maxIndice) with chain length of \(maxValue)")
    return maxIndice
}

maxFinder(p: 1000000)                                   // All that is left is for you to enter the limit :)