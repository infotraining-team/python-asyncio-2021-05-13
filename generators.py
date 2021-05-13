def generator():
    for i in range(4):
        yield i

print(type(generator))
print(type(generator()))

for i in generator():
    print(i)

g = generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))