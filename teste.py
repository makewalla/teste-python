print("ola mundo")

def soma (a,b):
    return f"a soma de {a} e {b} é {a+b}"

def subtracao (a,b):
    return f"a subtracao de {a} e {b} é {a-b}"

def divisao (a,b):
    if b!=0:
        return f"a divisao de {a} e {b} é {a/b}"
    else:
        return f"o numero não pode ser dividido por 0"    

def multiplicacao (a,b):
    return f"a multiplicao de {a} e {b} é {a*b}" 

def resto_div (a,b):
    return f"o resto de divisão de {a} e {b} é {a%b}"

opcao = None

while opcao !=0:

    opcao = int(input("digite 1 para soma | digite 2 para subtracao | digite 3 para divisão | digite 4 para multiplicação | digite 5 para resto da divisão | digite 0 para encerrar: "))
    
    if opcao==0:
        print("programa encerrado!")
        break
    elif opcao >0 and opcao <6:
        a = float(input("informe o primeiro numero: "))
        b = float(input("informe o segundo numero: "))       
        if opcao ==1:
            print(soma(a,b))
        elif opcao ==2:
            print(subtracao(a,b))
        elif opcao==3:
            print(divisao(a,b))
        elif opcao==4:
            print(multiplicacao(a,b))
        elif opcao==5:
            print(resto_div(a,b))    
    else:
        print("opção invalida")
          
