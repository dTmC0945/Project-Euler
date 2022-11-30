func primeCounter(n: Int) -> Int {                                          // primeCounter function takes number of
                                                                            // primes needed (n).

    var iter = 2
    var sieve = [Int]()                                                     // Array for putting the found primes
    var number = 2                                                          // Numbers to check for primes (start 2).

    while (sieve.count < n) {
        while (iter <= number) {

            outerLoop: for subLooper in 2...iter {
                if (iter % subLooper == 0 && iter != subLooper) {           // Check if the number divides that is not
                                                                            // equal to number (i.e., 2 divides 4. If
                    break outerLoop                                         // this happens exit the loop.
                } else if (iter % subLooper == 0 && iter == subLooper) {    // Otherwise the number is a prime and add
                    sieve.append(iter)                                      // it to the list.
                }
            }
            iter += 1
        }
        number += 1
    }

    print("\(n)st prime is: \(sieve[n - 1])")                               // print the final result.
    return 0                                                                // return 0 for a success :)
}

primeCounter(n: 10001)