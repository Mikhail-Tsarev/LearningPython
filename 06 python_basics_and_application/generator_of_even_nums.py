from itertools import takewhile


def even_gen():
    i = 2
    while True:
        yield i
        i += 2

b = even_gen()
result = list(takewhile(lambda x: x < 100, even_gen()))
print(result)
for i in range(20):
    print(next(b))