# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res += v
#     print(res)
#
# s(5, 5, 5, 5, 1)

def c(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c(n - 1, k) + c(n-1, k-1)

n, k = map(int, input().split())

print(c(n, k))
