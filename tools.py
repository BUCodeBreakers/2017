import math

def text_to_int(text):
    """
    Converts text into an integer for use in encryption.
    input: text - a plaintext message
    output: integer - an integer encoding text
    """
    integer = 0
    for char in text:
        if integer > 0:
            integer = integer*256
        integer = integer + ord(char)
    return integer

def int_to_text(i):
    """
    Converts an integer into text.
    input: i - an integer
    output: text - text represented by i
    """
    text = ""
    power = math.log(i, 256)
    while power > 0:
        digit = i % 256
        text = str(unichr(digit)) + text
        i = (i - digit) / 256
        power -= 1
    return text

def find_root(x, r):
    """
    Finds the integer component of the r'th root of x.
    https://stackoverflow.com/questions/356090/how-to-compute-the-nth-root-of-a-very-big-integer
    inputs:
        x - an integer whose rth root is to be found
        r - an integer root value
    output: an integer y such that y ** r <= x < (y + 1) ** r
    """
    high = 1
    while high ** r < x:
        high *= 2
    low = high / 2
    while low < high:
        mid = (low + high) / 2
        if low < mid and mid ** r < x:
            low = mid
        elif high > mid and mid ** r > x:
            high = mid
        else:
            return mid
    return mid + 1

def extended_gcd(a, b):
    """
    Given integers a and b, returns integers r, s and t such that
    r = s * a + t * b, and r is the greatest common denominator of a and b.
    inputs:
        a - an integer
        b - an integer
    outputs:
        r - the greatest common denominator of a and b
        s
        t
    """
    if b < 0: b = -b
    r1 = a; r2 = b
    s1 = 1; s2 = 0
    t1 = 0; t2 = 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - (q * r2); r1 = r2; r2 = r
        s = s1 - (q * s2); s1 = s2; s2 = s
        t = t1 - (q * t2); t1 = t2; t2 = t
    return (r1, s1, t1)

def combine_moduli(n1, n2, x1, x2):
    """
    Given integers x1 mod n1 and x2 mod n2,
    returns x such that n = n1 * n2, x mod n1 = x1, and x mod n2 = x2.
    inputs:
        n1 - a modulus
        n2 - a modulus
        x1 - a value modulo n1
        x2 - a value modulo n2
    output:
        x - a value modulo n1n2 such that x mod n1 = x1 an x mod n2 = x2.
    """
    (gcd, inv_n1_mod_n2, inv_n2_mod_n1) = extended_gcd(n1, n2)
    # make sure that n1 and n2 are relatively prime:
    assert gcd == 1, "Please make sure n1 and n2 are relatively prime."
    n = n1 * n2
    x = ((inv_n1_mod_n2 * n1 * x2) + (inv_n2_mod_n1 * n2 * x1)) % n
    while x < 0: x += n # make sure x is positive
    return x
