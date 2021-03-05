import itertools as it

for n in it.count():
    if 1000 < n < 1010:
        print(n);
    if n > 10000:
        break
