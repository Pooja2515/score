class Solution:
    def sumFourDivisors(self, nums):
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        total = 0

        for n in nums:

            p = 2
            while p * p * p <= n:
                if p * p * p == n and is_prime(p):
                    total += 1 + p + p*p + n
                    break
                p += 1
            else:
               
                divisors = []
                for i in range(2, int(n ** 0.5) + 1):
                    if n % i == 0:
                        j = n // i
                        divisors.append((i, j))
                        if len(divisors) > 1:
                            break

                if len(divisors) == 1:
                    i, j = divisors[0]
                    if i != j and is_prime(i) and is_prime(j):
                        total += 1 + i + j + n

        return total

