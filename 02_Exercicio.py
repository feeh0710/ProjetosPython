cont = 1
nota = 0
while cont <= 4:
    entrada = input(f'DIGITE A {cont}ª Nota: ')
    nota+=float(entrada)
    cont+=1
media = nota/4
print('A MÉDIA É: ',media)
if media <= 5:
        print('PARABENS VOCE SE LASCOU :P')
else:
        print('PARABENS VOCE PASSOU')
