foo = set()

for i in range(42):
    foo.add('Cake')

foo.add('Hello')
foo.add('World')

print(len(foo))
print(foo)

x_coordinate = (42,)

print(type(x_coordinate))