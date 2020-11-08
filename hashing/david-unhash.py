import hashlib
import time

given_hash = input("please input hash: ")

md4 = hashlib.md5

t0 = time.time()
for i in range(1000000000):
    if i % 1000000 == 0:
        print(i)
    if md4((str(i)).encode("utf-8")).hexdigest() == given_hash:
        print("number: ", i)
        break

print(time.time() - t0)