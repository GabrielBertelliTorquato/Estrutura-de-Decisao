# 1.Atribua valores para as variáveis usadas e determine o resultado da execução dos
# algoritmos abaixo:

numero = int(input("Digite um número: "))

if numero >= 20 and numero <= 90:
    print("Número no intervalo [20,90]")
else:
    print("Número fora do intervalo [20,90]")



a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))


if c > 5:
    d = (a - b) * c
else:
    d = (a + b) * c


print("O resultado da expressão é:", d)

# 2. Ler um valor e escrever se é positivo, negativo ou zero.

escreva_um_valor = float(input('Digite um valor: '))

if escreva_um_valor >= 0:
    print ('Este valor é positivo')
else:
    print('Este valor é negativo')

# 3.Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10,
# caso contrário escrever NÃO É MAIOR QUE 10!

digite_um_valor = float(input('Digite um valor: '))

if digite_um_valor >10:
    print ('É MAIOR QUE 10!')
else:
    print ('NÃO É MAIOR QUE 10!')

# 4.Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2

if soma > 10:
    print (soma)
else:
    print ('A soma não é maior que 10')

# 5.Entrar com um número e informar se ele é divisível por 5.

digite_um_numero = int(input('Digite um número: '))

calculo = digite_um_numero % 5

if calculo == 0:
    print('É divisível por 5')
else:
    print('Não é divisível por 5')

# 6.Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

digite_um_numero  = float(input('Digite um número: '))

if digite_um_numero >= 20 and digite_um_numero <= 90:
    print('Este número esta entre 20 e 90')
else:
    print('Este número não esta entre 20 e 90')

# 7.Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a
# pessoa nasceu).

ano_de_nascimento = int(input('Digite o ano em que você nasceu: '))

calculo = ano_de_nascimento - 2005

if ano_de_nascimento <= 2005:
    print ('Você pode votar este ano')
else:
    print ('Você não pode votar este ano')

# 8.Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o
# ano digitado é válido.

ano_de_nascimeto = int(input('Digte o ano em que você nasceu: '))

calculo = 2023 - ano_de_nascimeto

if ano_de_nascimeto <= 2023:
    print('Você tem {} anos'.format(calculo))
else:
    print('Esta data não é válida')

# 9.Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.

idade = int(input('Digite a idade da pessoa: '))


if idade >= 18 and idade <= 65:
    print('Maior de idade')
elif idade < 18:
    print('Menor de idade')
else:
    print('Acima de 65 anos')

# 10. Ler as notas da 1a e 2a avaliações de um aluno. Calcular a média aritmética simples e
# escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a
# nota for igual ou maior que 6 o aluno é aprovado). Escrever também a médiacalculada.~

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print('Você foi aprovado, sua media é de {}'.format(media))
else:
    print('Você foi reprovado, sua media é de {}'.format(media))

# 11. Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra
# “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja
# inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta
# média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário
# deve escrever “Reprovado”.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2


if media >= 7.0:
    print("Aprovado")
elif media < 7.0:
    nota_exame = float(input("Digite a nota do exame: "))
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aprovado")
    else:
        print("Reprovado")

# 12. Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores
# e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem
# salário total maior.

professor1horas = int(input('Digite a quantidade de aulas dadas pelo professor 1: '))
professor2horas = int(input('Digite a quantidade de aulas dadas pelo professor 2: '))

valorporhoraprof1 = float(input('Digite quantos o professor 1 ganha por hora: '))
valorporhoraprof2 = float(input('Digite quantos o professor 2 ganha por hora: '))

calculoprof1 = valorporhoraprof1 * professor1horas
calculoprof2 = valorporhoraprof2 * professor2horas

if calculoprof1 > calculoprof2:
    print ('Professor 1 ganha mais, {} reais'.format(calculoprof1))
elif calculoprof2 > calculoprof1:
    print('Professor 2 ganha mais, {} reais'.format(calculoprof2))
else:
    print ('Os professores tem salários iguais')

# 13. Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se
# este número é par ou ímpar.

numero = int(input('Digite um número: '))

calculo = numero % 2

if calculo == 0:
    print('Este número é par')
else:
    print('Este número é ímpar')

# 14. Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do
# vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time_casa = input('Digite o nome do time da casa: ')
time_visitante = input('Digite o nome do time visitante: ')

golstimecasa = int(input('Digite o número de gols do time da casa: '))
golstimevisit = int(input('Digite o número de gols do time visitante: '))

if golstimecasa > golstimevisit:
    print ('{} venceu'.format(time_casa))
elif golstimevisit > golstimecasa:
    print ('{} venceu'.format(time_visitante))
else:
    print ('A partida ficou empatada')

# 15. Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca,
# Paulista, Mineiro ou Outros”

sigla = input('Digite a sigla do seu estado: ')

if sigla.upper() == 'RJ':
    print ('Carioca')
elif sigla.upper() == 'SP':
    print ('Paulista')
elif sigla.upper() == 'MG':
    print ('Mineiro')
else:
    print('Outros')

# 16. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor
# da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o
# valor do produto e imprimir o valor da venda.

valor_compra = float(input("Digite o valor de compra do produto: R$ "))

if valor_compra < 20.00:
    margem_lucro = 0.45
else:
        margem_lucro = 0.30

valor_venda = valor_compra * (1 + margem_lucro)

print("O valor de venda do produto é: R$ {:.2f}".format(valor_venda))

# 17. Entrar com um número de 1 a 12 e exibir o mês correspondente.

mes = int(input('Digite o número do mês: '))

match mes:
    case 1:
      print('Janeiro')
    case 2:
      print('Fevereiro')
    case 3:
      print('Março')
    case 4:
      print('Abril')
    case 5:
      print('Maio')
    case 6:
      print('Junho')
    case 7:
      print('Julho')
    case 8:
      print('Agosto')
    case 9:
      print('Setembro')
    case 10:
      print('Outubro')
    case 11:
      print('Novembro')
    case 12:
      print('Dezembro')
    case _:
      print('Número invalido')

# 18. Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.")
elif letra.isalpha():
    print("A letra digitada é uma consoante.")
else:
    print("O caractere digitado não é uma letra.")

# 19. Ler 2 valores (considere que não serão lidos valores iguais) e escrever o maior deles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print ('{}'.format(n1))
elif n2 > n1:
    print ('{}'.format(n2))
else:
    print ('Os número são iguais')

# 20. Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem
# crescente.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('{}, {}'.format(n2, n1))
elif n2 > n1:
    print ('{}, {}'.format(n1, n2))
else:
    print ('Os valores são iguais')

# 21. Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior
# deles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
     print ('{}'.format(n1))
elif n2 > n1 and n2 > n3:
     print ('{}'.format(n2))
elif n3 > n1 and n3 > n2:
     print ('{}'.format(n3))
else:
  print ('Os números são iguais')

# 22. Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma
# dos 2 maiores.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

maior1 = max(valor1, valor2, valor3)
maior2 = 0
if maior1 == valor1:
    maior2 = max(valor2, valor3)
elif maior1 == valor2:
    maior2 = max(valor1, valor3)
else:
    maior2 = max(valor1, valor2)

soma = maior1 + maior2

print("A soma dos 2 maiores valores é:", soma)

# 23. Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em
# ordem crescente.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    if valor2 < valor3:
        print("Valores em ordem crescente:", valor1, valor2, valor3)
    else:
        print("Valores em ordem crescente:", valor1, valor3, valor2)
elif valor2 < valor1 and valor2 < valor3:
    if valor1 < valor3:
        print("Valores em ordem crescente:", valor2, valor1, valor3)
    else:
        print("Valores em ordem crescente:", valor2, valor3, valor1)
else:
    if valor1 < valor2:
        print("Valores em ordem crescente:", valor3, valor1, valor2)
    else:
        print("Valores em ordem crescente:", valor3, valor2, valor1)

#24.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:
    conceito = "E"

("Notas: ", nota1, ", ", nota2)
print("Média: ", media)
print("Conceito: ", conceito)
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")

# 25. Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem
# executadas (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação
# e 4 – Divisão). Calcular e escrever o resultado dessa operação sobre os dois valores
# lidos.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

operacao = int(input("Escolha a operação a ser executada (1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

if operacao == 1:
    resultado = valor1 + valor2
elif operacao == 2:
    resultado = valor1 - valor2
elif operacao == 3:
    resultado = valor1 * valor2
elif operacao == 4:
  
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        print("Erro: Divisão por zero não é permitida!")
        resultado = None
else:
    print("Erro: Opção de operação inválida!")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)

# 26

import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2 * a)
    print("A equação possui uma raiz real:", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("A equação possui duas raízes reais:")
    print("Raiz 1:", raiz1)
    print("Raiz 2:", raiz2)   

# 27

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Os valores lidos não formam um triângulo.") 

# 28

opcao = int(input("Digite a opção (1, 2 ou 3): "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if opcao == 1:
    valores = [a, b, c]
    valores.sort()
    print("Valores em ordem crescente: ", valores)
elif opcao == 2:
    valores = [a, b, c]
    valores.sort(reverse=True)
    print("Valores em ordem decrescente: ", valores)
elif opcao == 3:
    if a > b and a > c:
        maior = a
        valores = [b, maior, c]
    elif b > a and b > c:
        maior = b
        valores = [a, maior, c]
    else:
        maior = c
        valores = [a, b, maior]
    print("Valores com o maior valor entre os outros dois: ", valores)
else:
    print("Opção inválida. Digite 1, 2 ou 3.")

# 29

salario_atual = float(input("Digite o salário atual do funcionário em R$: "))

if salario_atual <= 400:
    indice_aumento = 15
elif salario_atual <= 700:
    indice_aumento = 12
elif salario_atual <= 1000:
    indice_aumento = 10
elif salario_atual <= 1500:
    indice_aumento = 7
elif salario_atual <= 2000:
    indice_aumento = 4
else:
    indice_aumento = 0

aumento = salario_atual * indice_aumento / 100
novo_salario = salario_atual + aumento

print("Índice de aumento: {}%".format(indice_aumento))
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Novo salário: R$ {:.2f}".format(novo_salario))

# 30

salario_atual = float(input("Digite o salário atual do funcionário em R$: "))

if salario_atual < 10000:
    reajuste = 55
elif salario_atual <= 25000:
    reajuste = 20
else:
    reajuste = 0

valor_reajuste = salario_atual * reajuste / 100
novo_salario = salario_atual + valor_reajuste

print("Valor do reajuste: R$ {:.2f}".format(valor_reajuste))
print("Novo salário: R$ {:.2f}".format(novo_salario))

# 31

temperatura = int(input("Digite a temperatura do forno em °C (inferior a 1000): "))

if temperatura <= 500:
    print("Temperatura Inválida")
elif temperatura < 700:
    print("Aquecimento Ligado em 100%")
elif temperatura < 735:
    print("Aquecimento Ligado em 50%")
elif temperatura >= 735 and temperatura <= 780:
    print("Aquecimento Desligado")
else:
    print("Superaquecimento")

# 32

valor = int(input("Digite um valor de 1 a 4: "))

if valor < 0 or valor > 4:
    print("Valor errado. Programa encerrado sem cálculos")
elif valor == 0:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("A soma dos números é:", resultado)
elif valor == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("A subtração dos números é:", resultado)
elif valor == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("A multiplicação dos números é:", resultado)
elif valor == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print("Erro: divisão por zero!")
    else:
        resultado = num1 / num2
        print("A divisão dos números é:", resultado)
elif valor == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 + num2) / 2
    print("A média dos números é:", resultado)

# 33. Escrever um algoritmo que leia valores inteiros em duas variáveis distintas e se o resto
# da divisão da primeira pela segunda for 1 mostre a soma dessas variáveis mais o resto
# da divisão; se for 2 escreva se o primeiro e o segundo valor são pares ou ímpares; se
# for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4 divida
# a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer
# outra situação mostre o quadrado dos números lidos.

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))

resto_divisao = valor1 % valor2

if resto_divisao == 1:
    soma = valor1 + valor2 + resto_divisao
    print("A soma dos valores mais o resto da divisão é:", soma)
elif resto_divisao == 2:
    if valor1 % 2 == 0 and valor2 % 2 == 0:
        print("Ambos os valores são pares.")
    elif valor1 % 2 != 0 and valor2 % 2 != 0:
        print("Ambos os valores são ímpares.")
    else:
        print("Os valores são mistos (um é par e o outro é ímpar).")
elif resto_divisao == 3:
    resultado = (valor1 + valor2) * valor1
    print("O resultado da multiplicação é:", resultado)
elif resto_divisao == 4 and valor2 != 0:
    resultado = (valor1 + valor2) / valor2
    print("O resultado da divisão é:", resultado)
else:
    quadrado1 = valor1 * valor1
    quadrado2 = valor2 * valor2
    print("O quadrado do valor 1 é:", quadrado1)
    print("O quadrado do valor 2 é:", quadrado2)

# 34. Escreva um algoritmo que leia as idades de 2 homens e 2 mulheres (considere que as
# idades dos homens serão sempre diferentes, bem como as das mulheres). Calcule e
# escreva a soma das idades do homem mais velho com a mulher mais nova, e o
# produto das idades do homem mais novo com a mulher mais velha.

idade_homem1 = int(input("Digite a idade do primeiro homem: "))
idade_homem2 = int(input("Digite a idade do segundo homem: "))
idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
idade_mulher2 = int(input("Digite a idade da segunda mulher: "))

soma_idades = max(idade_homem1, idade_homem2) + min(idade_mulher1, idade_mulher2)
produto_idades = min(idade_homem1, idade_homem2) * max(idade_mulher1, idade_mulher2)

print("A soma das idades do homem mais velho com a mulher mais nova é:", soma_idades)
print("O produto das idades do homem mais novo com a mulher mais velha é:", produto_idades)

# 35

numero = int(input("Digite um número de 4 dígitos (entre 1000 e 9999): "))

dezena_unidade = numero % 100
milhar_centena = numero // 100

terceiro_numero = dezena_unidade + milhar_centena

if terceiro_numero ** 2 == numero:
    print("O número", numero, "obedece à característica descrita.")
else:
    print("O número", numero, "não obedece à característica descrita.")
