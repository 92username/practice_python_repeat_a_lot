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

nome = "Vinicius"
idade = 45

print(f"O meu nome é {nome} e tenho {idade}")

### Exercício 2:
# Atribua valores a três variáveis `a`, `b`, e `c`. 
# Troque os valores de `a` e `b` 
# sem usar uma variável auxiliar e exiba o resultado.

a = 5
b = 15
c = 35
print(f"A lista original é {a}, {b} e {c}")
a,b = b,a
print(f"A nova lista após a troca é {a}, {b} e {c}")

# ### Exercício 3:
# Calcule a área de um círculo. Peça ao usuário o valor do raio e 
# armazene o resultado em uma variável chamada `area`. A fórmula para a área é:
# ```
# area = pi * raio^2
# ```
# Use `pi = 3.14159`.

raio = float(input("Digite o valor do raio para calcular a área do círculo: "))
pi = 3.14159
area = pi * (raio ** 2)
print(f"A área do círculo é {area:.4f}")

### Exercício 4:
# Atribua uma string de texto contendo um número (por exemplo, "25") a 
# uma variável. 
# Converta essa string para um número inteiro e exiba o dobro do valor.

algumtexto = "25"
algumtexto = int(algumtexto)
print(f"O dobro do valor é {algumtexto * 2}")

### Exercício 5:
# Crie duas variáveis: `preco` e `desconto`. Atribua valores a elas. 
# Calcule o preço final após o desconto e exiba o resultado.

preco = 3000
desconto = 0.25
preco_final = preco - (preco * desconto)
print(f"O preço original é {preco:.2f} reais. O valor do desconto é 25%. 
      O preço com desconto é {preco_final:.2f} reais.")

# Crie uma variável chamada nome e outra chamada idade. Atribua valores 
# a elas e exiba:
# Meu nome é <nome> e tenho <idade> anos.
nome = "Kardian"
idade = 1
print(f"Meu carro é um {nome} e ele tem {idade} ano de uso.")

# Crie duas variáveis a e b com valores inteiros. Troque os valores sem 
# usar uma variável auxiliar.

a ,b = 7, 49 # multiple assignment or unpacking
print(f"As variáveis originais são {a} e {b}")
a,b = b,a
print(f"As novas variáveis são {a} e {b}")

# Armazene dois números inteiros nas variáveis x e y. Calcule e exiba a 
# soma, subtração, multiplicação e divisão entre eles.

x, y = 7, 3
soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y

print(f"A soma é {soma}, a subtração é {subtracao}, a multiplicação é 
      {multiplicacao} e a divisão é {divisao:.2f}")

# defina 3 variaveis raio, pi e circunferencia. calcule a circunferencia.

raio = float(input("Digite o raio para calcular a circunferencia: "))
pi = 3.14159
circunferencia = pi * 2 * raio
print(f"A circunferencia mede : {circunferencia}.")
