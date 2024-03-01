import random

class RSA:
    def __init__(self, p, q):
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        self.public_key, self.private_key = self.generate_key_pair(p, q)

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def mod_inverse(e, phi):
        m0, x0, x1 = phi, 0, 1
        while e > 1:
            q = e // phi
            phi, e = e % phi, phi
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def generate_key_pair(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = self.gcd(e, phi)
        d = self.mod_inverse(e, phi)
        return (n, e), (n, d)

    def encrypt(self, plaintext):
        n, e = self.public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext):
        n, d = self.private_key
        decrypted = [chr(pow(char, d, n)) for char in ciphertext]
        return ''.join(decrypted)


# Example usage
def main():
    miras = RSA(17, 19)
    erda = RSA(17, 11)

    message = "Miras samiy top"
    print("Original message:", message)

    encrypted_message = miras.encrypt(message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = erda.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()
