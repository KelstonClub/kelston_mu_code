import hashlib
import time

hash_value = "131bb9703cedbd45e631a96b101a0259"
length = 8
maximum_range = 10**length

def test_hash_value(current_number):
    return hashlib.md5(str(current_number).encode("utf-8")).hexdigest()


def run():
    for current_number in range(maximum_range):
        if test_hash_value(current_number) == hash_value:
            print("Number found: ", current_number)
            break

t0 = time.time()
run()
print(time.time() - t0)