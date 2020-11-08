import hashlib
import itertools
import time

t0 = time.time()

md5 = hashlib.md5
hash_to_match = "131bb9703cedbd45e631a96b101a0259"

digits = [str(i).encode("utf-8") for i in range(10)]
for n, i in enumerate(itertools.product(digits, repeat=8)):
    s = b"".join(i)
    if n % 1000000 == 0: print(s)
    if md5(s).hexdigest() == hash_to_match:
        print("Found it -- %s" % s)
        break

print(time.time() - t0)
