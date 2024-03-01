# inspired by community solution
def solve():
    n = 600851475143
    i = 2
    factors = []
    while i * i <= n:
        # if not prime, move on
        if n % i:
            i += 1

        # add to prime numbers list and repeat 
        else:
            n //= i
            factors.append(i)
    
    # append last factor
    factors.append(n)
    return factors
            
            
if __name__ == '__main__':
    print(solve())
