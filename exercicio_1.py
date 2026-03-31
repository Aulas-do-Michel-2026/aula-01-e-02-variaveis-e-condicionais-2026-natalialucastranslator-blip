"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""
nota1 = float(input ("Digite a primeira nota:"))
nota2 = float(input ("Digite a segunda nota:"))
nota3 = float(input ("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3

print("A média das três notas do aluno é =", round(media, 2))
