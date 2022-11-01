
// Declare variables

var iter = 1        // iteration number
var sum = 0         // actual sum
var cache = 0       // value in the loop

// main loop

while(iter < 1000) {
    if(iter % 3 == 0 || iter % 5 == 0){
        cache = iter
        sum = sum + cache
    }
    iter = iter + 1
}

print(sum)