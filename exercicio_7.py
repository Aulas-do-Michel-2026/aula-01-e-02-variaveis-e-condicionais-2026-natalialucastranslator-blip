freq_pop = float(input("Digite a frequencia populacional (em porcentagem): "))
gene = input("Digite o gene: ").upper()
impacto = input("Digite o Impacto (ALTO ou BAIXO): ").upper()
reads = int(input("Digite os reads: "))
vaf = float(input("Digite a frequencia alélica (em porcentagem): "))

# Lista de genes de exceção
genes_excecao = ["HFE", "MEFV", "GJB2"]

# Verifica qualidade da leitura
if reads < 10 or vaf < 20:
    print("Resposta: Não é relevante.")
else:
    # Verifica impacto
    if impacto != "ALTO":
        print("Resposta: Não é relevante.")
    else:
        # Verifica frequência populacional
        if freq_pop > 5 and gene not in genes_excecao:
            print("Resposta: Não é relevante.")
        else:
            print("Resposta: É relevante.")
