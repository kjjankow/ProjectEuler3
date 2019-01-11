# Project Euler #3 - Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

theNumber = 10    # Sets end point of finding primes
primeList = []        # Initializes empty list of prime numbers
primeFactors = []     # Initializes empty list of prime factors for theNumber

for primeCan in range (2, theNumber):    # Looping through "prime candidates" between 2 and end
    isPrime = True                       # Initialize prime to be True until shown not to be
    for i in range(2, primeCan):         # Loops through 2 to primeCan to see if divisible. If not, PRIME
        if primeCan % i == 0:
            isPrime = False
    if isPrime:
        primeList.append(primeCan)       # Adds prime to the list

for i in range(0,len(primeList)):
    if theNumber % primeList[i] == 0:
        primeFactors.append(primeList[i])

print(primeList)
print(primeFactors)

