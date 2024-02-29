# Just for text

import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a prime number with a specified number of bits
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the modular multiplicative inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA key pair
def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose a public exponent e(1 < e < phi and gcd(e, phi) = 1)
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
    # Calculate the private exponent d, which is the modular multiplicative inverse of e modulo phi        
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Function to encrypt a plaintext message using RSA public key
def encrypt(public_key, plaintext):
    n, e = public_key
    # Convert each character in the plaintext to its corresponding ciphertext using modular exponentiation
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Function to decrypt a ciphertext message using RSA private key
def decrypt(private_key, ciphertext):
    n, d = private_key
    # Convert each ciphertext character back to its original plaintext using modular exponentiation
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

def main():
    bits = 16  # Adjust the number of bits as needed for your security requirements
    public_key, private_key = generate_keypair(bits)
    
    message = "Hello Erda"
    print("Original message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
