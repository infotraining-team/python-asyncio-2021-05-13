def is_prime(n):
    if n <= 1: return False
    elif n == 2: return True
    else:
        for div in range(2, n):
            if n % div == 0:
                return False
        else:
            return True

def primes_up_to(n):
    return [i for i in range(n+1) if is_prime(i)]

if __name__ == "__main__":
    assert primes_up_to(11) == [2, 3, 5, 7, 11]

