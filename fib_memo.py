from functools import lru_cache


# O(2^n)
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#d = fib(35)
# print(d)


def memo(num):
    mem = {}
    if num in mem:
        return mem[num]
    if num <= 2:
        return 1
    if num > 2:
        value = memo(num-1) + memo(num-2)
    mem[num] = value
    return value


# y = memo(35)  # 9227465
# print(y)


@lru_cache
def fib_cache(n):
    if n in {0, 1}:
        return n
    else:
        return fib_cache(n-1) + fib_cache(n-2)


#f = fib_cache(90)
# print(f)
