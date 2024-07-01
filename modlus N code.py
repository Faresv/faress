import math
import time
import random

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

def factorize(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return i, N // i
    return None, None

def generate_rsa_keys(bits):
    while True:
        p = generate_random_prime(bits)
        q = generate_random_prime(bits)
        if p != q:
            break
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 65537 
    d = pow(e, -1, phi)
    return N, e, d, p, q

def encrypt(message, e, N):
    encrypted_message = [pow(ord(char), e, N) for char in message]
    return encrypted_message

def decrypt(encrypted_message, d, N):
    decrypted_message = ''.join([chr(pow(char, d, N)) for char in encrypted_message])
    return decrypted_message

def main():
    test_cases = [8, 16]
    results = []

    for bits in test_cases:
        for _ in range(2): 
            N, e, d, p, q = generate_rsa_keys(bits)
            print(f"Testing with {bits}-bit values:")
            print(f"N: {N}")
            
            start_time = time.perf_counter()
            found_p, found_q = factorize(N)
            end_time = time.perf_counter()
            
            if found_p is not None and found_q is not None:
                print(f"p: {found_p}, q: {found_q}")
            else:
                print("Failed to factorize N.")
            
            runtime = (end_time - start_time) * 1000  
            print(f"Runtime: {runtime:.6f} milliseconds\n")
            results.append((bits, N, e, d, found_p, found_q, runtime))
    
    print(f"{'Bits':<10} {'N':<20} {'e':<10} {'d':<20} {'P':<10} {'Q':<10} {'Runtime/ms':<15}")
    for bits, N, e, d, p, q, runtime in results:
        print(f"{bits:<10} {N:<20} {e:<10} {d:<20} {p:<10} {q:<10} {runtime:<15.6f}")
        print(f"Public Key: (N={N}, e={e})")
        print(f"Private Key: (N={N}, d={d})")
        
        
        message = "Hello"
        print(f"Original Message: {message}")
        
        
        encrypted_message = encrypt(message, e, N)
        print(f"Encrypted Message: {encrypted_message}")
        
        
        decrypted_message = decrypt(encrypted_message, d, N)
        print(f"Decrypted Message: {decrypted_message}\n")

if __name__ == "__main__":
    main()
