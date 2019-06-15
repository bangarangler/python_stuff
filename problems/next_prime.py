'''
returns a generator that will yield an unlimited number of primes, starting
from the first prime (2)
prime number is any whole number that has exactly two divisors: one and the
number itself. first few primes are 2,3,5,7,11
'''

def next_prime():
  num = 2
  all_primes = set()
  while True:
    for prime in all_primes:
      if num % prime == 0:
        break
    else:
      all_primes.add(num)
      yield num
    num += num % 2 + 1

