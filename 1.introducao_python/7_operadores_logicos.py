# and or not

operador = not ( (5 == 7 or 3 > 2) and (2 == 2 or 5 < 5) )
#                  false     true        true      false
#                     \      /              \      /
#                       true        =         true
#                             not true = false

print(operador)