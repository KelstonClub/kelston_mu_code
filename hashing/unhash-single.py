import sys
import hashlib
import time

md5 = hashlib.md5
def hash(n):
    return n, md5(str(n).encode("utf-8")).hexdigest()

def main(hashed_target, length):
    length = int(length)
    for n in range(10**length):
        if hashed_target == md5(str(n).encode("utf-8")).hexdigest():
            print(n, "=>", hashed_target)
            break

if __name__ == '__main__':
    t0 = time.time()
    main(*sys.argv[1:])
    print(time.time() - t0)
