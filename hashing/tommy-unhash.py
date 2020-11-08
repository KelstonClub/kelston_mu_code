from hashlib import md5
import string
import time

def crack(hash, lenght):
     for i in range(int("9"*lenght)):
         guess = str(i)
         if md5(guess.encode("utf-8")).hexdigest() == hash:
            return guess

if __name__ == '__main__':
    hash = "131bb9703cedbd45e631a96b101a0259" # "70f80550589de85735a41c420ab69ae8" #"275cfee74a07eb927b3e08742ed6bd90"
    t0 = time.time()
    print(crack(hash, 10))
    print(time.time() - t0)