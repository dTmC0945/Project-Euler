import Swift
import Foundation

func primeFinder(n: Int) -> Int {                               // primeFinder function that takes an input number
                                                                // n : the number and produces the prime factors.
                                                                // return 0 upon completion
    var iter = 2                                                // iterator value set to one as you are starting from
                                                                // 2 as 1 is not a prime :)
    var sieve = [Int]()                                         // create an array to put the prime factors

    while (iter <= Int(sqrt(Double(n)))) {                      // main loop that checks all value up to sqrt(n)

        innerLoop: if (n % iter == 0) {                         // checks if the iterator divides with n
            if (sieve.count > 1) {                              // this loop checks whether the iterator value matches
                for i in 1..<sieve.count {                      // with a multiple value in the sieve array. This allows
                    if (iter % sieve[i] == 0) {                 // it to skip a lot of numbers, speeding up the loop
                        break innerLoop                         // if a value matches immediately break the loop and
                    }                                           // start the process all over again.
                }
            }
            sieve.append(iter)                                  // add the prime number to the array
            print(iter)                                         // print the prime numbers
        }
        iter += 1                                               // increase the iterative value by one.
    }

    return 0
}

primeFinder(n: 600851475143)                                    // Enter the huge number here.