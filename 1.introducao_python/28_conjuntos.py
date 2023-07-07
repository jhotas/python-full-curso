# Conjunto não permite dados repetidos

x = {1, 2, 3, 4, 5}
y = {2, 5, 7, 8, 10}

uniao = x.union(y)
intersecao = x.intersection(y)
diferenca = x.difference(y)
diferenca_simetrica = x.symmetric_difference(y)

print(uniao)
print(intersecao)
print(diferenca)
print(diferenca_simetrica)