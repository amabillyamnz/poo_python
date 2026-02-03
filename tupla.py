cores = ["azul", "vermelho", "preto", "marrom", "roxo"]
indice = int(input("Digite um número entre 0 a 4: "))

if (indice >= 0) and (indice < len(cores)):
    print(cores[indice])
else:
    print("Número invalido!")