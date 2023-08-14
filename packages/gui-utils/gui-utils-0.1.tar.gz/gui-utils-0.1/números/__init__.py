def fatorial(num):
    f = 1
    for c in range(1,num+1):
        f*=c
    return f
def dobro(num):
    return num * 2
def triplo(num):
    return num * 3
def quatruplo(num):
    return num * 4
def media(num,num2):
    numo = (num,num2)
    m = numo / 2
    return m
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("ERRO!: Digite um número inteiro válido")
def contador(começo=0,fim=0):
    import time
    for c in range(começo,fim+1):
        print(c)
        time.sleep(0.1)
    if c == fim:
        print("Fim!")
    return
def aumentar(número=0,porcentagem=0):
    return número + (número * porcentagem/100)
def metade(n):
    met = n / 2
    return(met)