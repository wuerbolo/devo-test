# Exercise1

## Execution

`python
python main.py -n <int number>
`

## Optimization

## 1. Improve upper limit from n/2 to sqrt(n)
After a bit of reading, we can improve the upper limit of our divisors checking. At first I went intuitively with n/2 for the worst case escenario of a number being a divisor. However, since n = a * b at the worst case, both are equal and their product can't exceed n, so, at its maximun, a divisor can be sqrt(n).

### Time of n/2 vs sqrt(n) for the first 100000 numbers:
- 153.47sec vs 14.13sec

## 2. Improve the number of divisors that we check
According to [this](https://math.stackexchange.com/questions/2920119/the-number-of-divisors-being-less-than-or-equal-to-twice-the-square-root-of-a-na) source we have:
d(n) <= 2 * sqrt(n)

So we can potentially shave off some iterations if we implement this check into the get_divisors function.
However, after trying this, apparently the opportunity never presents itself to use this as an early exit for the algorithm(at least not with the numbers I've tried)

## 3. Skip known prime numbers from divisor calculation
Since we have to potentially check for big numbers, upon finding a number that its prime, we don't have to check for future divisors.
Two things can be done to further improve here:
    - start checking for numbers that all the way to its square root don't have any divisor to include them on a prime dictionary, so that each time they reappear on another iteration we can save some time "calculating" their primes.
    - we could also download a list of primes and just 

## 4. Store divisors of previous calculations
We can store the divisors of the numbers we check so that if a greater multiple of them is asked we can skip that section of the divisor calculation.

