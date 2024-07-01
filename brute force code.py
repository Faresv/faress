import random
import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        prime_candidate |= (1 << bits - 1) | 1  
        if is_prime(prime_candidate):
            return prime_candidate

def generate_rsa_keys(bits):
    while True:
        p = generate_random_prime(bits)
        q = generate_random_prime(bits)
        if p != q:
            break
    N = p * q
    e = 65537  
    return N, e

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, N):
    gcd, x, y = gcd_extended(e, N)
    if gcd != 1:
        return None
    else:
        return x % N

def brute_force_private_exponent(N, e):
    for d in range(1, N):
        if (d * e) % N == 1:
            return d
    return None

def main():
    test_cases = [8, 16]
    results = []

    for bits in test_cases:
        for _ in range(2):
            N, e = generate_rsa_keys(bits)
            print(f"Testing with {bits}-bit values:")
            print(f"N: {N}, e: {e}")

            start_time = time.time()
            d = brute_force_private_exponent(N, e)
            end_time = time.time()

            runtime = (end_time - start_time) * 1000
            print(f"Runtime: {runtime:.2f} milliseconds")

            results.append((bits, N, e, d, runtime))

    print("\nResults:")
    print("Bits | N | e | d | Runtime (ms)")
    for result in results:
        bits, N, e, d, runtime = result
        print(f"{bits} | {N} | {e} | {d} | {runtime:.2f}")

if __name__ == "__main__":
    main()
