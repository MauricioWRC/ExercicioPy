def ex1():
    i = 0
    while i<=100:
        print(i)
        i+=1

#------------------------------------------
def ex2():
    i=50
    while i<=100:
        print(i)
        i+=1
def ex3():
    i=10
    while i>=0:
        print(i)
        i-=1
    print("Fogo!")

def ex4():
    numero = int(input("Digite um numero: "))
    i=1
    while i<=numero:
        print(i)
        i+=2
def ex5():
    numero = int(input("Digite um numero: "))
    i=0
    while i<=numero:
        print(i)
        i+=3
def ex6():
    numero = int(input("Digite um numero para a tabuada: "))
    i = 1
    while i<=10:
        calc = i*numero
        print(f"{numero} * {i} = {calc}")
        i+=1
def ex7():
    numero = int(input("Digite um numero para a tabuada: "))
    inicio = int(input("Digite um numero para o inicio: "))
    fim = int(input("Digite um numero para o fim: "))
    while inicio<=fim:
        calc = inicio*numero
        print(f"{numero} * {inicio} = {calc}")
        inicio+=1
def ex8():
    primeiro = int(input("Digite o primeiro numero: "))
    segundo = int(input("Digite o segundo numero: "))
    contador = 1
    calc = 0
    while contador<=primeiro: #Aqui ele vai criar um contador para fazer a soma determinadas vezes
        calc+= segundo #Realizando a soma em loop
        print(calc)
        contador+=1
def ex9():
    primeiro = int(input("Digite o primeiro numero: "))
    segundo = int(input("Digite o segundo numero: "))
    calc = primeiro
    i = 0
    while (calc-segundo)>=0:
        print(calc)
        calc-= segundo
        i+=1
    print(f"A divisão: {primeiro}/{segundo} é de {i} e com uma resto de {calc}")
def ex10():
    Primeira = str(input("Qual a soma de 4+4: A:3; B:8; C:10; D:20--> ")).lower()
    Segunda = str(input("Qual a soma de 5*4: A:20; B:8; C:10; D:15--> ")).lower()
    Terceira = str(input("Qual a soma de 4/2: A:3; B:8; C:10; D:2--> ")).lower()
    contador = 0
    if Primeira == 'b' or Segunda=='a' or Terceira=='d':
        if Primeira == 'b':#AQUI PRECISA SER IF E N ELIF PARA QUE ELE POSSA LER OS PROXIMOS
            contador+=1
        if Segunda=='a': #AQUI PRECISA SER IF E N ELIF PARA QUE ELE POSSA LER OS PROXIMOS
            contador+=1
        if Terceira=='d':
            contador+=1
        print(f"Você acertou {contador} questões")
    else:
        print('Você n acertou nenhuma. Tente novamente!')

def ex11():
    Deposito = int(input('Deposito inicial: R$:'))
    juros = int(input("Juros mensal em %: "))/100
    contador = 0
    while contador<24:
        contador+=1
        taxa = Deposito*juros
        Deposito+=taxa
        print(f"No mes {contador} o valor em conta será de R$:{Deposito:.2f}")


def ex12():
    Deposito = float(input('Deposito inicial: R$:'))
    juros = float(input("Juros mensal em %: "))/100
    contador = 0
    DepositoM = 0
    while contador<24:
        DepositoMensal = int(input('Deposito mensal R$:'))
        Deposito+=DepositoMensal
        contador+=1
        taxa = (Deposito)*juros
        Deposito+=taxa
        print(f"No mes {contador} o valor em conta será de R$:{Deposito:.2f}")

def ex13():
    divida = float(input("Valor da divida: "))
    taxa= float(input("Valor da taxa mesal em %: "))/100
    valor = float(input("Valor mensal a depositado: "))
    contador = 0
    while divida>=0:
        if valor<=0:
            print('Caloteiro safado!!')
            break
        divida-=valor
        divida+=divida*taxa
        contador+=1
        if divida<=valor:
            print(f"Você pagara por {contador} meses e no ultimo mês terá que pagar apenas R${divida:.2f} para zerar sua divida")
            break

def ex14():
    Numero = int(input('Digite um numero inteiro: '))
    contador = 0
    Soma = 0
    while Numero!= 0:
        contador+=1
        Soma+= Numero
        print("Para finalizar o processo digite o valor de 0")
        Numero = int(input('Digite um numero inteiro: '))
    aritimetica = Soma/contador
    print(f"Foram digitados {contador} numero, sua soma foi de {Numero} e a média aritimetica de {aritimetica}")

def ex15():
    codigo = input('''Produtos
          Código 1 - Proço R$ 0,50
          Código 2 - Proço R$ 1,00
          Código 4 - Proço R$ 4,00
          Código 5 - Proço R$ 7,00
          Código 9 - Proço R$ 8,00
          Digite 0 para finalizar a compra
        Codigo: ''')
    contador = 0
    valor =0
    while codigo!="0":
        if codigo == "1":
            valor+=0.5

        if codigo == "2":
            valor+=1

        if codigo=="4":
            valor+=4

        if codigo=="5":
            valor+=7

        if codigo=="9":
            valor+=8
        print(f"Valor total: {valor}")
        if codigo!='1' and codigo!='2' and codigo!='4' and codigo!= '5' and codigo!='9' and codigo!='0':
            print('Codigo invalido')
            contador-=1
        if codigo == '0':
            break
        codigo = input("Codigo: ")
        contador+=1
    print(f'''Quantidades de itens: {contador} 
Valor total: {valor}''')


def ex16():
    valor = int(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    while valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')
        valor = int(input("Insira o valor: R$ "))
def ex17():
    valor = 0
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')

def ex18():
    valor = int(input("Insira o valor: R$ "))
    notas100=0;nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    if valor>0:
        while valor>=100:
            notas100+=1
            valor-=100
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
    print(f'''Foram utilizados:
{notas100} notas de 100
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1''')

def ex19():
    valor = float(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    moedas1 =0;moedas2 =0;moedas5 =0;moedas10 =0;moedas50=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        while valor>=0.5:
            moedas50+=1
            valor-=0.49
        while valor>=0.1:
            moedas10+=1
            valor-=0.1
        while valor>=0.05:
            moedas5+=1
            valor-=0.05
        while valor>=0.02:
            moedas2+=1
            valor-=0.02
        while valor>=0.01:
            moedas1+=1
            valor-=0.01

    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1
{moedas50} moedas de 50
{moedas10} moedas de 10
{moedas5} moedas de 5
{moedas2} moedas de 2
{moedas1} moedas de 1
''')

def ex20():
    valor = float(input("Insira o valor: R$ "))
    nota50 = 0;nota20=0;nota10=0;nota4=0;nota1=0
    moedas1 =0;moedas2 =0;moedas5 =0;moedas10 =0;moedas50=0
    if valor>0:
        while valor>=50:
            nota50+=1
            valor-=50
        while valor>=20:
            nota20+=1
            valor-=20
        while valor>=10:
            nota10+=1
            valor-=10
        while valor>=4:
            nota4+=1
            valor-=4
        while valor>=1:
            nota1+=1
            valor-=1
        while valor>=0.5:
            moedas50+=1
            valor-=0.49
        while valor>=0.1:
            moedas10+=1
            valor-=0.1
        while valor>=0.05:
            moedas5+=1
            valor-=0.05
        while valor>=0.02:
            moedas2+=1
            valor-=0.02
        while valor>=0.01:
            moedas1+=1
            valor-=0.01

    print(f'''Foram utilizados:
{nota50} notas de 50
{nota20} notas de 20
{nota10} notas de 10
{nota4} notas de 4
{nota1} notas de 1
{moedas50} moedas de 50
{moedas10} moedas de 10
{moedas5} moedas de 5
{moedas2} moedas de 2
{moedas1} moedas de 1
''')
    if valor<0.01 and valor!=0:
        print(f'Valor abaixo do esperado: {valor}')

def ex21():
    return ex16()

def ex22():
    loop = True
    while loop == True:
        menu = str(input('''MENU
ADIÇÃO          --> [1]
SUBTRAÇÃO       --> [2]
DIVISÃO         --> [3]                
MULTIPLICAÇÃO   --> [4]                  
SAIR            --> [5]        

OPÇÃO DESEJADA: '''))
        if menu == '1':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor a somar: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} + '))
                resultado += Numero1
            print(f"O valor das somas foi de {resultado}")
        if menu == '2':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor a subtrair: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} - '))
                resultado -= Numero1
            print(f"O valor das subtrações foi de {resultado}")
        if menu == '3':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor dividir: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} / '))
                resultado /= Numero1
            print(f"O valor das divisões foi de {resultado}")
        if menu == '4':
            print("Digite 0 para voltar ao menu")
            Numero = float(input('Digite o primerio valor multiplicar: '))
            Numero1 = None
            resultado = Numero
            while Numero1 != 0 and Numero!=0:
                Numero1 = int(input(f'{resultado} * '))
                resultado *= Numero1
            print(f"O valor das somas foi de {resultado}")
        if menu == '5':
            loop = False

funciona= True
while funciona == True:
    escolha = int(input('''Escolha um exercicio para ver a funcionalidade
exercicios disponiveis do 1 ao 22 e digite 0 para sair,
apenas digitar o numero do exercicio que funcionará no seu termianl, tmj
                    
Numero do exercicio: '''))
    if escolha == 0:
        funciona == False
        break
    if escolha == 1:
        ex1()
    if escolha == 2:
        ex2()
    if escolha == 3:
        ex3()
    if escolha == 4:
        ex4()
    if escolha == 5:
        ex5()
    if escolha == 6:
        ex6()
    if escolha == 7:
        ex7()
    if escolha == 8:
        ex8()
    if escolha == 9:
        ex9()
    if escolha == 10:
        ex10()
    if escolha == 11:
        ex11()
    if escolha == 12:
        ex12()
    if escolha == 13:
        ex13()
    if escolha == 14:
        ex14()
    if escolha == 15:
        ex15()
    if escolha == 16:
        ex16()
    if escolha == 17:
        ex17()
    if escolha == 18:
        ex18()
    if escolha == 19:
        ex19()
    if escolha == 20:
        ex20()
    if escolha == 21:
        ex21()
    if escolha == 22:
        ex22()


