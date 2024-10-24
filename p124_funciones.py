# p124-funciones

def leerdatos():
    datos=[]
    while True:
        d = int(input("Numero: "))
        if d==-1: break
        datos.append(d)
    return datos

def mayor (lista):
    m = lista[0]
    for n in lista:
        if n>m:
            m = n
    return m

def menor (lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def promedio(nums):
    s=0
    for n in nums:
        s += n
    p = s / len(nums)
    return p

pi = 3.1416
gt = 9.7242343

