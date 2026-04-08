cromossomo = input("Digite o cromossomo: ")
posicao = int(input("Digite a posição: "))
genoma = input("Digite o genoma de referência: ")

# Verificando se está no BRCA1
if cromossomo == "chr17":
    if genoma == "hg19":
        if 41196312 <= posicao <= 41277500:
            print("Sim")
        else:
            print("Não")
    elif genoma == "hg38":
        if 43044295 <= posicao <= 43125483:
            print("Sim")
        else:
            print("Não")
    else:
        print("Não")
else:
    print("Não")
