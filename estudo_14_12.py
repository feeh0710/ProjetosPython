operacao = 1

while(operacao == 1):
    iteracao = int(input("DIGITE A ITERACAO: "))
    cont = 1
    while(cont <= iteracao):
        print(cont)
        if (cont == 5):
            print("CINCO")
        elif (cont == 2):
            print("DOIS")
        cont += 1
    print(" 0 = não \n 1 = sim")
    operacao = int(input("DESEJA FAZER NOVAMENTE A OPERAÇÃO? "))  



##TABOADA
    for x in range(1,11):
        print("TABOADA DO ",x)
        for y in range(1,11):
            print(f"{x} * {y} = ",(x*y))
        






