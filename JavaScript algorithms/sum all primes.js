//sum all primes
function sumPrimes(num) {
  function isPrime(num) {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i == 0) return false;
    }
    return true;
  }

  let res = 0;
  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) {
      res += i;
    }
  }
  return res;
}

sumPrimes(10);