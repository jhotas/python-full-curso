# Receba uma temperatura em farenheit e exiba em celsius.
# c = 5 * ((f - 32)/9)

print('---CONVERSOR FARENHEIT-CELSIUS---\n')
temp_f = float(input('Digite a temperatura em graus farenheit: '))
temp_c = 5 * ((temp_f - 32)/9)

print(f'A temperatura em graus celsius é de {temp_c}')