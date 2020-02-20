# # Exercicio 1 ---------------------------------------- se o numero é ou nao é maior que 10

# x = int(input('Inform a number: '))

# if x > 10:
#     print('{} é maior que 10'.format(x))
# else:
#     print('{} é menor que 10'.format(x))


# Exercicio 2 --------------------------- numero positivo ou negativo

# x = int(input("Inform a number:"))
# if x < 0:
#     print('{} is negative'.format(x))
# else:
#     print('{} is positive'.format(x))

# ## Exercicio 3 ------------------------------------  Compra de macas

# apple = 1.30
# apple2 = 1
# apples = int(input('Inform how many apples you will buy? '))

# if apples < 12:
#     print('Your purchase will cost: $ {}'.format(apple * apples))
# else:
#     print('Your purchase will cost: $ {}'.format(apple2 * apples))

# # Exercicio 4 --------------------------- Aluno aprovado ou reprovado

# nota1 = float(input('Inform the note number 1: '))
# nota2 = float(input('Inform the note number 2: '))
# average = (nota1 + nota2) / 2

# if average >= 6:
#     print('Congratulations you were approved!, your average: {}'.format(average))
# else:
#     print('Excuse me, you were disapproved, your average: {} '.format(average))


#Exercicio 4  ------------------------------------ Se podera ou nao votar

# import datetime 

# birth = int(input('informe the your year of birth: '))
# year = 2020

# calc = year - birth
# if calc >= 18:
#     print('Congratulations you can vote this year, Idade: {}'.format(calc))
# else:
#     print('Ops, your not can vote this year Idade: {}'.format(calc))


# #Exercicio 5 ---------------------------------Mior numero entrw dois informados

# value = int(input('Inform a number: '))
# value2 = int(input('Inform a number: '))
# if value == value2:
#     print('Os valores nao podem ser iguais')
# else:
#     print("Maior valor é: {}".format(max(value, value2)))

# Exercicio 6 ---------------------------------  em ordem crescente

# values = []
# value = input('Inform number 1: ')
# value1 = input('Inform number 2: ')
# if value == value1:
#     print('Values ​​cannot be the same')
# else:
#     if value > value1:
#         print(value1, value)
#     else:
#         print(value, value1)

## Exercicio 7 ---------------------------------------------------- Jogo de xadrez

# hourIni = int(input('Inform the hour initial of game: '))
# hourEnd = int(input('Inform the hour end of game: '))
# day = 24
# if hourEnd == hourIni:
#     print('Duracao do jogo: {}:00 horas'.format(day))
# else:
#     if hourEnd < hourIni:
#         duracao = (day - hourIni) + hourEnd
#         if duracao > day:
#             print('Nao é permitido duracao do jogo maior que 24 horas: {}'.format(duracao))
#         print('Duracao: {}'.format((day - hourIni) + hourEnd))
#     else:
#         print(hourEnd - hourIni)

# # Exercicio 8 ------------------------------------  Horas trabalhadas

# weeks = []
# s1 = weeks.append((int(input('Informe o total de horas trabalhadas na 1ª semana: '))))
# s2 = weeks.append((int(input('Informe o total de horas trabalhadas na 2ª semana: '))))
# s3 = weeks.append((int(input('Informe o total de horas trabalhadas na 3ª semana: '))))
# s4 = weeks.append((int(input('Informe o total de horas trabalhadas na 4ª semana: '))))
# salary = float(input('informe salario: '))

# hours_worked = sum(weeks)
# Value_hours = salary / (4 * 40)
# hours_positive = hours_worked - (4 * 40)

# if hours_positive > 0:
#     hours_extras = Value_hours * 0.5

#     value_total = (hours_extras + Value_hours) * hours_positive
#     salario_total = value_total + salary
#     print('Seu salario do mes com {} horas extras: R$ {}, reais'.format(hours_positive, salario_total))
# else:
#     print('Voce nao teve horas extras esse mes')

# Exercicio 9 ------------------------------------------------ peso ideal por sexo

# name = input("inform your name: ")
# gender = input('inform your gender: M for man or F for woman: ')
# stature = float(input('Inform your stature: '))
# peso_ideal = 0

# if gender == 'M':
#     peso_ideal = (72.7 * stature) - 58
# else:
#     peso_ideal = (62.1 * stature) - 44.7
# print("{} Your peso ideal is: {}".format(name, peso_ideal))

# Exercicio 10 ------------------------------------- Salary_Com comisao de vendas
# Salary_fixed = float(input('Inform your salary fixed: R$ '))
# value_total_sales = float(input('Inform the value total in sales: R$ '))
# salary_total = 0
# if value_total_sales <= 1500:
#     salary_total = (value_total_sales * 0.03) + Salary_fixed
# else:
#     salary_total = (value_total_sales * 0.05) + Salary_fixed
# print('Your salary total this month is: R$ {}'.format(salary_total))

#Exercicio 11 ----------------------------------- Saldo bancario
# balance = float(input('Inform your bank balance: '))
# debit = float(input('Inform the your value in debit: '))
# credit = float(input('Inform the your value in credit: '))
# balance_atual = balance - debit + credit
# if balance_atual > 0:
#     print('Your bank balance this Positive: balance: $ {}'.format(balance_atual))
# elif balance_atual == 0:
#     print('yout bank balance this zeroed: $ {}'.format(balance_atual))
# else:
#     print('Your bank balance this negative: $ {}'.format(balance_atual))

#Exercicio 12 ------------------------------- Produto em stoque
# amoult_actual = float(input('Inform the amoult actual of product in stock: '))
# amoult_max = float(input('inform the amoult max of product: '))
# amoult_minimun = float(input('inform the amoult minimun of product: '))
# amoult_average = (amoult_max + amoult_minimun) / 2
# if amoult_actual >= amoult_average:
#     print('No reality purchase')
# else:
#     print('reality purchase')

#Exercicio 13 ------------------------------ Value maior, menor ou igual a zero
# valueA = float(input('Inform 1º value: '))
# if valueA > 0:
#     print('Value {} great than zero'.format(valueA))
# elif valueA == 0:
#     print('Value {} equal the zero'.format(valueA))
# else:
#     print('Value {} smalle than zero'.format(valueA))

#Exercicio 14 ------------------------------ Maior valor entre tres  nao iguais
# value1 = float(input('Inform 1º value: '))
# value2 = float(input('Inform 2º value: '))
# value3 = float(input('Inform 3º value: '))
# if value1 == value2 or value1 == value3 or value2 == value3:
#     print('values ​​cannot be equals')
# else:
#     print('the greatest value: {}'.format(max(value1, value2, value3)))

#Exercicio 15 -----------------------------Soma dos dois maiores numeros de uma lista
# import heapq

# valores = []
# value1 = valores.append(float(input('Informe 1º value: ')))
# value2 = valores.append(float(input('Informe 2º value: ')))
# value3 = valores.append(float(input('Informe 3º value: ')))

# if value1 == value2 or value1 == value3 or value2 == value3:
#     print('values cannot be equals')
# values_max = heapq.nlargest(2, valores)
# print('A soma dos dois maiores numeros: {}'.format(sum(values_max)))

# Exercicio 16 --------------------------- ordernamdo em ordem crescente os tres numeros informados
# values = []
# value1 = values.append(input('Inform the 1º value: '))
# value2 = values.append(input('Inform the 2º value: '))
# value3 = values.append(input('inform the 3º value: '))
# if value1 == value2 or value3 == value1 or value2 == value3:
#     print('Values cannot be equals')
# values = sorted(values)
# print('Em ordem crescente: {}'.format(values))

# Exercicio 17 ------------------------ Se forma ou nao um triangulo
# a = float(input('Inform the side a of triangle: '))
# b = float(input('Inform the side a of triangle: '))
# c = float(input('Inform the side a of triangle: '))
# if a + b > c and c + b > a and c + a > b:
#     print('its a triangle')
# else:
#     print('No is a triangle')

# Exercicio 18 --------------------- Placar de futebol 
# import random
# name_team_a = input('Inform the name of team A: ')
# name_team_b = input('Inform the name of team B: ')
# gols_team_a = random.randint(0,5)
# gols_team_b = random.randint(0,5)
# if gols_team_a > gols_team_b:
#     print('Placar: {} - 0{} X 0{} - {}'.format(name_team_a, gols_team_a, gols_team_b, name_team_b))
#     print('Team {} Win.'.format(name_team_a))
# elif gols_team_b > gols_team_a  :
#     print('Placar: {} - 0{} X 0{} - {}'.format(name_team_a, gols_team_a, gols_team_b, name_team_b))
#     print('Team {} Win.'.format(name_team_b))
# else:
#     print('Placar: {} - 0{} X 0{} - {}'.format(name_team_a, gols_team_a, gols_team_b, name_team_b))
#     print('Empate')

# Exercicio 19 -------------------------- Comparando dois numeros
# number_a = float(input('Inform the 1º number: '))
# number_b = float(input('Inform the 2º number: '))
# if number_a > number_b:
#     print('First is bigger: a: {} and b: {}'.format(number_a, number_b))
# elif number_b > number_a:
#     print('Second is bigger: a: {} and b: {}'.format(number_a, number_b))
# else:
#     print('Numbers equals: a: {} and b: {}'.format(number_a, number_b))

# Exercicio 20 --------------------------- Desconto posto de combustivel
# combustivel = input('Informe o combustivel: A para alcool e G para Gasolina: ')
# litros = float(input('Informe a quantidade de litros da compra: '))
# preco_A = 2.9
# preco_G = 3.3

# if combustivel == 'A':
#     if litros <= 20:
#         preco_total =  litros * (preco_A * 0.03)
#         print('Preco a pagar: R$ {}'.format(preco_total))
#     else:
#         preco_total = litros * (preco_A * 0.05)
#         print('Preco a pagar: R$ {}'.format(preco_total))
# else:
#     if litros <= 20:
#         preco_total = litros * (preco_G * 0.04)
#         print('Preco a pagar: R$ {}'.format(preco_total))
#     else:
#         preco_total = litros * (preco_G * 0.06)
#         print('Preco a pagar: R$ {}'.format(preco_total))

#Exercicio 21 ------------------------------------- Fera de frutas
# kg_total = 0
# apple = 0
# strawberry = 0
# cost_total = 0
# cost_apple = 1.8
# cost_strawberry = 2.5
# spin = True
# while spin:
#     fruit = input('Informe a fruta desejada: Mg para morango e Mc para maca: ')
#     kg = float(input('Informe quantos kg: '))
#     if fruit == 'Mg':
#         apple += kg
#         if kg <= 5:
#             cost_total += kg * 2.5
#         else:
#             cost_total += kg * 2.2
#     elif fruit == 'Mc':
#         strawberry += kg
#         if kg <= 5:
#             cost_total += kg * 1.8
#         else:
#             cost_total += kg * 1.5
#     response = input('Deseja realizar mais uma compra? sim ou nao: ')
#     if response != 'sim':
#         spin = False

# kg_total += apple + strawberry
# if kg_total > 8 or cost_total > 25:
#     cost_total = cost_total - (cost_total * 0.1)
#     print('Preco a pagar: ${:.2f} que equivale a {:.2f}kg em frutas, maca: {:.2f}kg e morango: {:.2f}kg'.format(cost_total, kg_total, apple, strawberry))
# else:
#     print('Preco a pagar: ${:.2f} que equivale a {:.2f}kg em frutas, maca: {:.2f}Kg e morango: {:.2f}kg'.format(cost_total, kg_total, apple, strawberry))

# Exercicio 22 ------------------------------------ acessando sistema
# 
# userId = int(input('informe seu id: '))
# if userId == 123123:
#     senhaUser = (int(input('Informe sua senha: ')))
#     if senhaUser == 9999:
#         print('Acesso permitido')
#     else:
#         print('Senha incorreta')
# else:
#     print('Usuario Invalido')

#Exercicio 23 -------------------------------------- desconto por compra de produtos
# name_product = input('Informe o nome do produto: ')
# amount_product = int(input('Informe a quantidade do produto: '))
# cost_unit = float(input('informe o preco por unidade do produto: '))
# cost_total = amount_product * cost_unit
# if amount_product <= 5:
#     cost_total = cost_total - (cost_total * 0.02)
#     print('Valor a pagar com 2% de desconto no produto {}: ${:.2f}'.format(name_product, cost_total))
# elif amount_product <= 10:
#     cost_total = cost_total - (cost_total * 0.03)
#     print('Valor a pagar com 3% de desconto no produto {}: ${:.2f}'.format(name_product, cost_total))
# else:
#     cost_total = cost_total - (cost_total * 0.05)
#     print('Valor a pagar com 5% de desconto no produto {}: ${:.2f}'.format(name_product, cost_total))

#Exercicio 24 ------------------------------------------ Media de aproveitamento do aluno
# grade1 = float(input('Informe a nota da prova 1: '))
# grade2 = float(input('Informe a nota da prova 1: '))
# grade3 = float(input('Informe a nota da prova 1: '))

# exercises_average = float(input('Informe a media dos exercicios: '))
# average_grades_student = ((grade3 * 3) + (grade2 * 2) + grade1 + exercises_average) / 7
# if average_grades_student >= 9:
#     print('Conceito do aluno: A {}')
# elif average_grades_student >= 7.5 and average_grades_student < 9:
#     print('Conceito do aluno: B')
# elif average_grades_student >= 6 and average_grades_student < 7.5:
#     print('Conceito do aluno: C')
# else:
#     print('Conceito do aluno: D')

#Exercicio 25 ----------------------------------------- Calculando a aposentadoria do funcionario
# from datetime import datetime

# employee_id = int(input('Informe o codigo do funcionario: '))
# if employee_id == 123:
#     year_birth = int(input('Informe o ano de nascimento do funcionario: '))
#     year_admission= int(input('Informe o ano de admissao do funcionario: '))
#     year_now = datetime.now().year
#     if  year_now - year_birth >= 65 or year_now - year_admission >= 30:
#         print('Requerer aposentadoria')
#     elif year_now - year_birth >= 60 and year_now - year_admission >= 25:
#         print('Requerer aposentadoria')
#     else:
#         print('Nao requerer aposentadoria')
# else:
#     print('Codigo invalido')


#--------------------------------------- REPETITIVE STRUCTURES -------------------------------------------------

# Exercicio 26 E 27 -------------------- Usando while par calcular dois valores
# valueA = float(input('Informe o valor de A: '))
# valueB = float(input('Informe o valor de B: '))
# if valueB == 0:
#     while valueB == 0:
#         print('o valor de B nao pode ser zero!')
#         valueB = float(input('Informe o valor de B: '))
#         if valueB > 0:
#             break
# print('resultado A / B : {:.2f}'.format(valueA / valueB))

#Exercicio 28 ------------------------------------ Usando while para calcular nota de tal aluno
# while True:
#     grade1a = float(input('Informe o valor da nota 1A: '))
#     grade2a = float(input('Informe o valor da nota 2A: '))
#     average_grade = (grade1a + grade2a) / 2

#     if grade2a and grade1a >= 0 and grade1a and grade2a <= 10:
#         print('Media do aluno: {:.2f}'.format(average_grade))
#     else:
#         print('informe notas de 1 a 10 apenas')
#     response = input('Novo calculo S/N?')
#     if response == 'S' or response == 'N':
#         if response == 'N':
#             print('Calculo finalizado')
#             break
#         else:
#             True
#     else:
#         response = input('Informe S ou N: ')
#         if response == 'N':
#             print('Calculo Finalizado')
#             break
#         else:
#             True

# Exercicio 29 ---------------------- imprime de 1 a 10 e de ordem crescente usando o while
# i = 0
# il = []
# while i < 10:
#     i += 1
#     il.append(i)
# print('valores: {}'.format(il))

# Exercicio 30 --------------------- Imprime de 1 a 10 de ordem decrescente usando o while
# lx = []
# x = 0
# while x < 10:
#     x += 1
#     lx.append(x)
# lx = sorted(lx, reverse=True)
# print('Valores: {}'.format(lx))

# Exercicio 31 -----------------------Imprime de 100 a 110 os 10 primeiros numeros inteiros
# lista_inteiros = []
# i = 100
# x = 110
# while i < x:
#     i += 1
#     lista_inteiros.append(i)
# print('Valores: {}'.format(lista_inteiros))

#Exercicio 32 e 33 ---------------------------- Imprime de 1 ao numero informado usando while
# lis_N = []
# n = int(input('Informe um numero: '))
# i = 0
# if n <= 0:
#         n = int(input('Informe um numero maior que 1: '))
# while i < n:
#     i+=1
#     lis_N.append(i)
# print('Valores: {}'.format(lis_N))

#Exercicio 34 --------------------------- Imprime a tabuada de 8 usando o while
# lis = []
# x = 8
# y = 0
# while x * y < 80:
#     y += 1
#     lis.append(x * y)
# print('Taboada de 8: {}'.format(lis))

#Exercicio 35 --------------------------- Imprime a tabuada do numero informado de 1 a 10 usando o while
# tab = []
# x = int(input('Informe um valor inteiro de 1 a 10: '))
# y = 0
# while x * y < x * 10:
#     if x <= 10:
#         y += 1
#         tab.append(x * y)
#     else:
#         x = int(input('Informe um valor inteiro menor que 10: '))
#         if x <= 10:
#             x * y < x * 10
# print('Tabuada do {}: {}'.format(x, tab))

# lista = []
# while len(lista) < 10:
#     x = int(input('Informe 10 numeros de 1 a 10, faltam {} numeros: '.format(10 - len(lista))))
#     lista.append(x)
# print('Numeros entre o intevalo [10 - 20]: {}'.format(lista[10:20]))
# print('Numeros entre o intervalo [0 - 9]: {}'.format(lista[0:9]))


# def print_n_to_x(n, x):
#     print(n)

#     if n < x:        
#         print_n_to_x(n+1, x)    

# n = 0
# x = 10
# print_n_to_x(n, x)

#  from math import factorial
# # def factor(y):
# #     if y > 1:
# #         return factor(y -1) * y
# #     else:
# #         return y
# y =  int(input('informe um valor: '))
# # print(factor(y))
# print(factorial(y))
# lista = [1,2,3]

# for i in enumerate(lista):
#     print(i, lista[2])

# teste ='abcde'

# print(teste.index('c'))

# retorna uma lista traves de uma funcao
# def pars(i):
#     if i % 2 == 0:
#         return i

# lista = [1,2,3,4,5,6,7,8,9]

# lista_par = filter(pars, lista)
# print(list(lista_par)) 

