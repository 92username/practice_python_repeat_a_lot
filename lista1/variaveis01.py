"""
Lista de exercicios - Manipulação de variáveis
"""
## 1. Manipulação de Variáveis

### Exercício 1:
# Crie uma variável chamada `nome` e atribua o valor do seu nome a 
# ela. Em seguida, crie outra variável chamada `idade` e atribua sua idade. 
# Exiba no console:
# ```
# Meu nome é <nome> e tenho <idade> anos.
# ```

NOME = "Vinicius"
IDADE = 45

print(f"O meu nome é {NOME} e tenho {IDADE}")

### Exercício 2:
# Atribua valores a três variáveis `a`, `b`, e `c`. 
# Troque os valores de `a` e `b` 
# sem usar uma variável auxiliar e exiba o resultado.

A = 5
B = 15
C = 35
print(f"A lista original é {A}, {B} e {C}")
A,B = B,A
print(f"A nova lista após a troca é {A}, {B} e {C}")

# ### Exercício 3:
# Calcule a área de um círculo. Peça ao usuário o valor do raio e 
# armazene o resultado em uma variável chamada `area`. A fórmula para a área é:
# ```
# area = pi * raio^2
# ```
# Use `pi = 3.14159`.

raio = float(input("Digite o valor do raio para calcular a área do círculo: "))
PI = 3.14159
area = PI * (raio ** 2)
print(f"A área do círculo é {area:.4f}")

### Exercício 4:
# Atribua uma string de texto contendo um número (por exemplo, "25") a 
# uma variável. 
# Converta essa string para um número inteiro e exiba o dobro do valor.

ALGUMTEXTO = "25"
ALGUMTEXTO = int(ALGUMTEXTO)
print(f"O dobro do valor é {ALGUMTEXTO * 2}")

### Exercício 5:
# Crie duas variáveis: `preco` e `desconto`. Atribua valores a elas. 
# Calcule o preço final após o desconto e exiba o resultado.

PRECO = 3000
DESCONTO = 0.25
PRECO_FINAL = PRECO - (PRECO * DESCONTO)
print(f"O preço original é {PRECO:.2f} reais."
      f"O valor do desconto é 25%. "
      f"O preço com desconto é {PRECO_FINAL:.2f} reais.")

# Crie uma variável chamada nome e outra chamada idade. Atribua valores 
# a elas e exiba:
# Meu nome é <nome> e tenho <idade> anos.
NOME = "Kardian"
IDADE = 1
print(f"Meu carro é um {NOME} e ele tem {IDADE} ano de uso.")

# Crie duas variáveis a e b com valores inteiros. Troque os valores sem 
# usar uma variável auxiliar.

A,B = 7, 49 # multiple assignment or unpacking
print(f"As variáveis originais são {A} e {B}")
A,B = B,A
print(f"As novas variáveis são {A} e {B}")

# Armazene dois números inteiros nas variáveis x e y. Calcule e exiba a 
# SOMA, subtração, multiplicação e divisão entre eles.

X, Y = 7, 3
SOMA = X + Y
SUBTRACAO = X - Y
MULTIPLICACAO = X * X
DIVISAO = X / Y

print(f"A SOMA é {SOMA}, a subtração é {SUBTRACAO},"
      f"a multiplicação é {MULTIPLICACAO} e a divisão é {DIVISAO:.2f}")

# defina 3 variaveis raio, pi e circunferencia. calcule a circunferencia.

raio = float(input("Digite o raio para calcular a circunferencia: "))
PI = 3.14159
circunferencia = PI * 2 * raio
print(f"A circunferencia mede : {circunferencia}.")
