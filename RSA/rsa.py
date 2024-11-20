from random import *

def gcd(m, n):
    # Base case: stop when the remainder is 0
    if m == 0:
        return n, 0, 1

    gcd_res, x1, y1 = gcd(n % m, m)

    x = y1 - (n // m) * x1
    y = x1

    return gcd_res, x, y


def keys(p, q):
    n = p * q
    phi_n = (p- 1) * (q - 1)

    # Find a number e that has only 1 as the gcd between e and phi_n
    e = randint(2, phi_n)
    while gcd(e, phi_n)[0] != 1:
        e = randint(2, phi_n)

    # Find d such that de ≡ 1 (mod phi_n)
    # gcd_res here is known to be 1
    # gcd_res = 1 = x.e + y.phi_n
    gcd_res, x, y = gcd(e, phi_n)
    d = x % phi_n # to make sure d is positive (d = |x|)

    return n, e, d

# return encrypted message c
def encrypt(m, n, e): 
    return pow(m, e, n)

# return decrypted message dcp_m
def decrypt(c, n, d):
    return pow(c, d, n)

def test():
    # two primes
    p = 1283
    q = 59
    n, e, d = keys(p, q)

    # 1000 random en/decryption instances
    for _ in range(1000):
        m = randint(1, n-1) # 0 < m < n; m: message to be encrypted
        c = encrypt(m, n, e)
        dcp_m = decrypt(c, n, d)
        assert dcp_m == m, f"Failed: m={m}, decrypted_m={dcp_m}"

def main():
    test()

if __name__ == "__main__":
    main()


