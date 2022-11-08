def add_func (n1, n2):
    return n1+n2

def min_func (n1, n2):
    return n1-n2

n1, n2, res = 100, 200, 0

res = add_func(n1, n2)
print(n1, "+", n2, "=", res)
res = min_func(n1, n2)
print(n1, "-", n2, "=", res)
