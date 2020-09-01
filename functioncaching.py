import time
from functools import lru_cache


@lru_cache(maxsize=3)   # Maxsize means it will cache/save the last "input in maxsize" numbers.
def work(n):
    # Some task taking n seconds
    time.sleep(n)

    return n

if __name__ == '__main__':
    print("Now running some work\n")
    work(3)
    work(2)  #This is the last value that will cache
    work(4)   #This is the second last value that will cache
    work(4)  #This is the first value that will cache
    print("done... calling again")
    work(3)  # It wont give a 3 second delay while using a decorator, this is called function caching.
    print("called again")