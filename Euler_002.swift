func fibonacci(n: Int) -> Int {     //Designing the fibonacci function

    var iter = 1                    // Fibonacci number iterator (start with 1)
    var cache_1 = 0                 // Cache for the first fibonacci number
    var cache_2 = 0                 // Cache for the second fibonacci number
    var cache_3 = 0                 // Cache for the third fibonacci number (i.e., sum)
    let limit = 4000000             // Limit imposed by the question
    var even_sum = 0                // Storage for the even numbered fibonacci numbers.


    // fib_(n) = fib_(n-1) + fib_(n-2)
    // cache_3 = cache_2   + cache_1

    while (iter <= n && (cache_2 + cache_1) < limit) {      // while-loop for the function
        if (iter == 1) {                                    // special case for fib_1 = 1
            cache_1 = 1
        } else if (iter == 2) {                             // special case for fib_2 = 2
            cache_2 = 2
        } else {
            cache_3 = cache_2 + cache_1                     // two previous values are added
            cache_1 = cache_2                               // fib_(n-2) is moved up to fib_(n-1)
            cache_2 = cache_3                               // fib_(n-1) is moved up to fib_(n)
        }
        if (cache_3 % 2 == 0){                              // finding the even valued fibonacci numbers
            even_sum += cache_3
            cache_3 = 0                                     // cleaning the cache_3 (just some tidying up :) )
        }

        iter += 1                                           // increase the while loop iterator
    }

    return even_sum                                         // function returns the even_sum
}

print(fibonacci(n: 40) + 2)                                 // prints the solution (n is arbitrary as long as
                                                            // the fibonacci number is higher than 4,000,000.
                                                            // two is added for the special case which is also
                                                            // divisible by 2.