## Exercícios
##- 1: Crie um programa para que apresente seu nome, seu celular e sua cidade.
##- 2: Crie um programa para que apresente sua idade, altura e peso.
##- 3: Crie um programa que contenha duas variáveis, um delas deve conter a matéria que você mais gosta e a outra uma frase sobre essa matéria. Apresente as duas frases juntas.

print('ESCOLHA O EXERCICIO \n 1- EXERCICIO1 \n 2- EXERCICIO2 \n 3- EXERCICIO3  ')
tipExercicio = input()
if tipExercicio == '1':
    print("INICIO PROGRAMA 1")
    nome,celular,cidade = 'Fernando','15991434950','Cesário Lange sp'
    print(f'Olá me chamo {nome}, meu telefone é o {celular} e a cidade é {cidade}!')
    print('#############   FIM EXERCICIO 1  ###################')
elif tipExercicio == '2':
    print('INICIO PROGRAMA 2')
    idade,altura,peso = 28 , 1.85 , '100KG'
    print(f'Olá tenho {idade} anos, minha altura é {altura} e meu peso é {peso}!')
    print('#############   FIM EXERCICIO 2  ###################')
elif tipExercicio == '3':
    print('INICIO PROGRAMA 3')
    materia,frase = 'Programação' , 'Hello World :)'
    print(f'Matéria Favorita: {materia}\nFrase sobre materia: {frase}!')
    print('#############   FIM EXERCICIO 3  ###################')
