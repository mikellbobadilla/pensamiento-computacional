def ejercicio_uno():
    primer = int(input('Ingresa el primer número: '))
    segundo = int(input('Ingresa el segundo número: '))
    
    es_grande = primer > segundo
    
    print(f'El primero es más grande: {es_grande}')
    
def ejercicio_dos():
    letra = input('Ingresa un letra cualquiera: ')
    
    no_es_vocal = letra.lower() not in ['a', 'e', 'i', 'o', 'u']
    
    print(f'El valor ingresado no es vocal: {no_es_vocal}')

def ejercicio_tres():
    numero = int(input('Ingresa un número culquiera: '))
    es_par_y_menor = numero % 2 == 0 and numero < 10

    print(f"El número es par y menor que 10: {es_par_y_menor}")

def ejercicio_cuatro():
    numero = int(input('Ingresa un número para obtener su valor absoluto: '))    

    def absoluto(num):
        return abs(num)
    
    print(f'El valor absoluto de {numero} es: {absoluto(numero)}')
    
def ejercicio_cinco():
    
    mensaje = "¡Juguemos!. Ingresá piedra(r), papel(p) o tijera(t): "
    claves = ['r', 'p', 't']
    
    valor = input(mensaje)
    
    no_es_valido = valor not in claves
    
    if no_es_valido:
        print('NO vale, el valor que ingresaste no sirve')    
        
    if valor == 'p':
        print('Tijera. ¡Te gané!')
    elif valor == 'r':
        print('Papel. ¡Te gané!')
    elif valor == 't':
        print('Piedra. ¡Te gané!')
    

def ejercicio_seis():
    limite = 200
    primero = int(input('Ingresa el primero número: '))
    segundo = int(input('Ingresa el segundo número: '))
    sumado = primero + segundo
    es_menor = sumado < limite
    
    if es_menor:
        cuanto_falta = limite - sumado
        print(f'La cantidad que falta para llegar a {limite} es: {cuanto_falta}')
    elif not es_menor:
        print('Llega a 100')
    

def ejercicio_siete():
    letra = input('Ingresa un letra inicial de las estacione de año: ').lower()
    def obtener_estacion(letra):
        estaciones = ['v', 'o', 'i', 'p']
        
        es_incorrecto = letra not in  estaciones
    
        if es_incorrecto:
            print('Error: El valor ingresado no es válido')
        elif letra == 'v':
            print('Verano')
        elif letra == 'o':
            print('Otoño')
        elif letra == 'i':
            print('Invierno')
        elif letra == 'p':
            print('Primavera')
        
    obtener_estacion(letra)

def ejercicio_ocho():
    numero = int(input('Ingrese un número entero: '))
    
    for n in range(1, numero + 1):
        print(n)
        

def ejercicio_nueve():
    numero = input('Ingresar un número: ')
    
    def operacion(numero, operador): 
        for n in range(1, 10 + 1):
            total = eval(numero + operador + str(n))
            print(f'{numero} {operador} {n} : {total}')    
    print("Suma")
    operacion(numero, "+")
    print("Resta")
    operacion(numero, "-")
    print("Multiplicación")
    operacion(numero, "*")
    
    
def ejercicio_diez():
    numero = int(input('Ingrese un número: '))
    
    for n in range(numero):
        print('Que los cumplas feliz!')

def ejercicio_once():
    importe = int(input('Ingrese el importe a pagar: '))
    
    def cobrador(importe):
        saldo_restante = importe
        
        while saldo_restante > 0:
            monto = int(input(f'El importe a pagar es de {saldo_restante}. Por favor, ingrese un monto'))
            saldo_restante -= monto
    
    cobrador(importe)

def ejercicio_doce():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f'El número {numero} es par')
        else:
            print(f'El numero {numero} es impar')
    
def ejercicio_trece():
    fichas_necesarias = 3
    ficha_costo = 'F'
    while fichas_necesarias > 0:
        ficha = input(f'Ingresá {fichas_necesarias} ({ficha_costo}) fichas para comenzar ')
        if len(ficha) == 1 and ficha in ficha_costo:
            fichas_necesarias -= 1
        else:
            print(f'Por favor solamente ingrese fichas reales ({ficha_costo})')

    print('¡A jugar!')
    
def ejercicio_catorce():
    numero = int(input('Ingresa un número: '))
    def es_primo(n):
        cantidad_divisible = 0
        for i in range(2, n):
            if n % i == 0:
                cantidad_divisible =+ 1
        return cantidad_divisible == 0      
    
    for n in range(1, numero + 1):
        if es_primo(n) == True:
            print(f'El número {n} es primo')


def main():
    ejercicio_catorce()
    
if __name__ == '__main__':
    main()