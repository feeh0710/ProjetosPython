
def criptografar(frase, chave):
    texto = ""
    for letra in frase:
        texto += f"{chr(ord(letra)+chave)}"
    print(texto)    

def descriptografar(frase , chave):
    texto = ""
    for letra in frase:
        texto+= f"{chr(ord(letra)-chave)}"
    print(texto)

criptografar("FERNANDO",25)
descriptografar("_^kgZg]h",25)
