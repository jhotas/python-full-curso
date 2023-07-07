x = [1, 2, 3]
y = x
z = y.copy()

print(hex(id(x)))
print(hex(id(y)))
print(hex(id(z)))