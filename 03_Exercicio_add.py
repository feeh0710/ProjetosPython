
#################################################
user = "fernando"
password = "123"

usuario = input("DIGITE SEU USUARIO: ")
senha =   input("DIGITE A SENHA: ")

if senha != "" and usuario != "" :
    if senha == password and usuario == user :
        print("LOGIN EFETUADO COM SUCESSO!")
           
    else :
        print("USUARIO OU SENHA INCORRETA!")

else :
    print("USUARIO OU SENHA NAO PODE ESTAR VAZIO")