import sys
from multiprocessing import Pool
import hashlib
import time

md5 = hashlib.md5
def hash(n):
    return n, md5(str(n).encode("utf-8")).hexdigest()

def main(hashed_target, length):
    length = int(length)

    with Pool() as pool:
        for n, hashed_n in pool.imap_unordered(hash, range(10**length), 10**4):
            if hashed_n == hashed_target:
                print(n, "=>", hashed_n)
                break

if __name__ == '__main__':
    t0 = time.time()
    main(*sys.argv[1:])
    print(time.time() - t0)
