import random

class RSA:
    def __init__(self, p, q):
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        self.public_key, self.private_key = self.generate_key_pair(p, q)
        self.friend_key = None

    @staticmethod
    # Function to check if a number is prime
    def is_prime(num): 
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    # Function to calculate the greatest common divisor (GCD) of two numbers
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    # Function to find the modular multiplicative inverse using extended Euclidean algorithm
    def mod_inverse(e, phi):
        m0, x0, x1 = phi, 0, 1
        while e > 1:
            q = e // phi
            phi, e = e % phi, phi
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Function to generate RSA key pair
    def generate_key_pair(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)
        # Choose a public exponent e(1 < e < phi and gcd(e, phi) = 1)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)
        # Calculate the private exponent d, which is the modular multiplicative inverse of e modulo phi 
        d = self.mod_inverse(e, phi)
        return (n, e), (n, d)

# Function to encrypt a plaintext message using RSA public key
    def encrypt(self, plaintext):
        n, e = self.public_key
        # Convert each character in the plaintext to its corresponding ciphertext using modular exponentiation
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext
    
    def encrypt_friend(self, plaintext):
        n, e = self.friend_key
        # Convert each character in the plaintext to its corresponding ciphertext using modular exponentiation
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

# Function to decrypt a ciphertext message using RSA private key
    def decrypt(self, ciphertext):
        n, d = self.private_key
         # Convert each ciphertext character back to its original plaintext using modular exponentiation
        decrypted = [chr(pow(char, d, n)) for char in ciphertext]
        return ''.join(decrypted)

    def encrypt_file(self, file_path):
        n, e = self.public_key
        encrypted_data = []

        with open(file_path, 'rb') as f:
            byte = f.read(1)
            while byte:
                encrypted_data.append(pow(int.from_bytes(byte, byteorder='big'), e, n))
                byte = f.read(1)

        return encrypted_data

    def decrypt_file(self, encrypted_data):
        n, d = self.private_key
        decrypted_data = []

        for num in encrypted_data:
            decrypted_data.append(pow(num, d, n))

        return decrypted_data



# Example usage
def main():
    miras = RSA(17, 19)
    erda = RSA(17, 11)

    miras.friend_key = erda.public_key
    erda.friend_key = miras.public_key

    message = "Miras samiy top"
    print("Original message:", message)

    encrypted_message = miras.encrypt_friend(message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = erda.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
