pais = input("Qual país você vai viajar? ")

if pais == "Estados Unidos":
    reais = float(input("Quantos reais você quer converter? "))
    dolares = reais / 5
    print(f"{dolares:.2f} USD")

elif pais == "Argentina":
    reais = float(input("Quantos reais você quer converter? "))
    pesos = reais * 180
    print(f"{pesos:.2f} ARS")

elif pais == "Japão":
    reais = float(input("Quantos reais você quer converter? "))
    ienes = reais * 30
    print(f"{ienes:.2f} JPY")

else:
    print("Não temos essa moeda em caixa.")
