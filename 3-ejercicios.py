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
    
    pass

def main():
    ejercicio_diez()
    
if __name__ == '__main__':
    main()