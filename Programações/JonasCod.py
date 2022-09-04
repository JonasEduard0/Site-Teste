'''     #Bibiotecas
from math import sqrt
from time import sleep
import random
salario = float(input("Insira o salário:"))
sleep(1)
print("Salário inicial é \033[4;31;42m{}\033[m".format(salario))
sleep(1)
print("Aumento de {}:".format(15/100*salario))
print("Salário final é {}".format(15/100*salario+salario))
raiz = sqrt(salario)
print('Raiz de salario é', raiz)
print("\n")

        #IF,else,elif
vc = input("Digite a letra:")
if vc == "a" or vc == "e" or vc == "i" or vc == "o" or vc == "u":
    print("Vogal")
if vc != "a" and vc != "e" and vc != "i" and vc != "o" and vc != "u":
    print("Consoante")
print("\n")

        #For, laço de repetição
i = int(input('I:'))
f = int(input('F:'))
p = int(input('P:'))
for c in range(i,f,p):
    print(c)
print('\n')

somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5): #4 vezes
    print('----- {} PESSOA -----'.format(p))#no lugar de {} sera colocado a posiçao da pessoa
    nome = input('Nome:').strip() #strip tira espaços desnecessarios
    idade = int(input('Idade:'))
    sexo = input('Sexo M/F:').strip()
    #aqui o comando pedira as informaçoes de 4 pessoas
    somaidade += idade
    if p == 1 and sexo in 'Mmmasculino':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
mediaidade = somaidade/4
print('A media de idade e {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idade, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher))
print('\n')

        #While, laço de repetição
co = 0
while co < 10:
    co += 1
    if co == 6 or co == 8:
        continue
    print(co)
print('\n')

conta = 0
while conta < 10:
    conta += 1
    if conta == 6:
        break
    print(conta)
print('\n')

nome = input('Olá! Qual seu nome? : ')
tentar = 1
resp = random.randint(1, 20)
adv = int(input('Certo {}, tente adivinhar o número entre 1 e 20 : '.format(nome)))
while tentar < 6 : 
    if adv < resp : 
        adv = int(input('O numero é maior, tente de novo : '))
        tentar += 1
    if adv > resp : 
        adv = int(input('O numero é menor, tente de novo : '))
        tentar += 1
    if adv == resp :
        print(input('Parabens, \033[4;31;42m{}\033[m! Você adivinhou em {} tentativas.'.format(nome, tentar)))
        break
    if tentar == 6 :
        print('Você excedeu o número de tentativas!')
        break
print('\n')

    #Variáveis compostas
        #Tuplas
lanche = 'H', 'S' , 'P', 'U'
print(lanche[1:])
for comida in lanche:
    print(f'Vou comer {comida}')
print(len(lanche))
del(comida)
print('\n')

        #Listas
cont = 'zero','um','dois','tres','quatro','cinco'
while True:
    nume = int(input('Numero entre 0 e 5: '))
    if 0 <= nume <= 5:
        break
print(f'Voce digitou o numero {cont[nume]}')
print('\n')

        #Dicionário
anime = {'titulo' : 'Another', 'ano' : 2012, 'diretor' : 'Matsumoto'}
print(anime.keys())
print(anime.items())
del anime['ano']

anime['temporada'] = 'Outono'

print(f'O anime {anime["titulo"]} foi lançado em {anime["temporada"]}')

for k, v in anime.items():  #items,values,keys
    print(f'O {k} é {v}')#k é keys e v é values
print('\n')

        #Função
def lin():
    print('-'*30)
lin()
print('Sistema de alunos')
lin()
print('Cadastro de funcionarios')
lin()
print('\n')

    #com parâmetros
def titulo(txt):#passar a quantidade de parametros q terá
    print('-'*30)
    print(txt)
    print('-'*30)
titulo('Curso em video')
titulo('Python e bom')
titulo('oi')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
valores = [7,2,5,0,4]
dobra(valores)
print(valores)

def area(l,c=0): #c = 0 para caso não for atibuido um valor(Parâmetro opcional)
    j = l*c      #Variável local
    print(j)
largura = float(input('largura: ')) #Variável global
comprimento = float(input('comprimento: '))
area(largura,comprimento)
print('\n')

def soma(a=0,b=0,c=0):
    s = a + b + c 
    return s        #Retorna s para cada variavel
r = soma(3,2,5)
r2 = soma(1,7)
r3 = soma(4)
print(f'Os calculos deram {r},{r2} e {r3}')

        #Interactive help
help()
help(print)

        #Exceção/Erro
try: 
    a = int(input('Numerador : '))
    b = int(input('Denominador : '))
    r = a / b #Se b receber 0, dará um erro,com esse comando você pode exibir uma mensagem caso dê erro
except Exception as erro: #Exception as variavel para mostrar o erro 
    print(f'Houve um problema!Ele é {erro.__class__}') #Há erro.class, cause, context, etc
except ValueError: #Pode ter uma mensagem expecífica para os erros
    print('O erro é de valor')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')'''