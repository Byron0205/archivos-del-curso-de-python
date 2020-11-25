def sumar(num1,num2):
    return num1+num2

def restar(num1, num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def repetir(func,a,b):
    return func(func(a,b), func(a,b))

num1=int(input("digite el primer numero: "))
num2=int(input("digite el segundo numero: "))
operacion=input("que operacion desea realizar: ")

multi=multiplicar(num1,num2)
if operacion=="sumar":
    print(sumar(num1, num2))

elif operacion=="restar":
    print(restar(num1,num2))

elif operacion=="multiplicar":
    print(multiplicar(num1, num2))

elif operacion== "multi":
    print(multi)

print(repetir(sumar,num1,num2))



