

def soma():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")

    

    A = int(a)
    B = int(b)

    resultadoSoma = A + B
    print("O resultado é: " , resultadoSoma)
    

def subtracao():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")

    A = int(a)
    B = int(b)

    resultadoSoma = A - B
    print("O resultado é: " , resultadoSoma)
        




def multiplicacao():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")

    A = int(a)
    B = int(b)

    resultadoSoma = A * B
    print("O resultado é: " , resultadoSoma)    


def divisao():
    a = input("Digite o primeiro número: ")
    b = input("Digite o segundo número: ")

    A = int(a)
    B = int(b)

    resultadoSoma = A / B
    print("O resultado é: " , resultadoSoma)    





def selecao(select):
    if(select == "1"):
        soma()
    elif(select == "2"):
        subtracao()
    elif(select == "3"):
        multiplicacao()
    elif(select == "4"):
        divisao()
    else:
        print("Por favor, selecione uma opção válida!")
        select = input("digite sua opção: ")
        selecao(select)


print("Bem vindo a minha primeira calculadora com Python!")
input("Pressiona Enter para continuar")
print("Digite 1 para Soma \nDigite 2 para Subtração \nDigite 3 para Multiplicação \nDigite 4 para Divisão")
select = input("Digite sua opção: ")
selecao(select)




















