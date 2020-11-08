import sys
import hashlib
import random

def main(length):
    length = int(length)
    n = random.randint(10**(length-1), 10**length)
    hashed = hashlib.md5(str(n).encode("utf-8")).hexdigest()
    print(n, "=>", hashed)

if __name__ == '__main__':
    main(*sys.argv[1:])
