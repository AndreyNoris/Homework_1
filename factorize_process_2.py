import time
from multiprocessing import Process


def check(number: int):
    is_prime = []
    for i in range(number + 1):
        if i != 0 and number % int(i) == 0:
            is_prime.append(i)
        else:
            continue
    return is_prime


def factorize(*numbers):
    checker = []
    for i in [*numbers]:
        checker.append(Process(target=check, args=(i,)).start())
    return checker


if __name__ == '__main__':
    start = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    finish = time.time() - start
    print(f'Time with one process: {finish}')
