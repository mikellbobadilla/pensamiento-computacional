def ejercicio_uno():
    numero = int(input('Ingrese un número entero: '))
    print(f'El número entero que ingresaste es {numero}')    
    
def ejercicio_dos():
    primer_numero = int(input('Ingrese el primer número: '))    
    segundo_numero = int(input('Ingrese el segundo número: '))
    
    suma = primer_numero + segundo_numero
    resta = primer_numero - segundo_numero
    producto = primer_numero * segundo_numero
    division = primer_numero // segundo_numero
    resto = primer_numero % segundo_numero
    
    print(f'La suma de {primer_numero} + {segundo_numero} es: {suma}')
    print(f'La resta de {primer_numero} - {segundo_numero} es: {resta}')
    print(f'La multiplicación de {primer_numero} * {segundo_numero} es: {producto}' )
    print(f'La división entera de {primer_numero} // {segundo_numero} es: {division}')
    print(f'El resto es la división de {primer_numero} % {segundo_numero} es: {resto}')


def ejercicio_tres():
    numero = int(input('Ingresa un número par o impar: '))
    
    if numero % 2 == 0:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} es impar')

def ejercicio_cuatro():
    anio_nacimiento = int(input('Ingrese su año de nacimiento: '))
    anio_posterior = int(input('Ingrese un año posterior a su año de nacimiento: '))
    
    if anio_posterior < anio_nacimiento:
        print('El año posterior es menor a su año de nacimiento. Intente otra vez.')
        return

    edad = anio_posterior - anio_nacimiento
    print(f'Tenias {edad} años en el año {anio_posterior}')
    
def ejercicio_cinco():
    numero = int(input('Ingrese el primer número entero: '))
    
    numero += int(input('Ingrese el segundo número entero: '))
    
    numero += int(input('Ingrese el tercer número entero: '))
    
    numero += int(input('Ingrese el cuarto número entero: '))
    
    numero += int(input('Ingrese el quinto número entero: '))
    
    print(f'El promedio es: {numero // 5}')

def ejercicio_seis():
    numero = int(input('Ingrese un número entero: '))
    
    print(f'El anterior y siguiente del número {numero} es: {numero - 1} y  {numero + 1}')
    
def ejercicio_siete():
    
    texto = input('Ingrese un texto cualquiera: ')
    numero = input('Ingrese un número entero cualquiera: ')
    
    def unir_texto():
        return texto + ' ' + numero
    
    texto_unido = unir_texto()
    
    print(f'El resultado es: "{texto_unido}"')
    
def ejercicio_ocho():
    primer = int(input('Ingrese el primer número: '))
    segundo = int(input('Ingrese el segundo número: '))
    
    # a.
    def resto(num1, num2):
        return num1 % num2
    # b.
    def cociente(num1, num2):
        return num1 / num2
    
    print(f'El resto de la división de los números {primer} y {segundo} es: {resto(primer, segundo)}')
    print(f'El cociente de la sivisión de los números {primer} y {segundo} es: {cociente(primer, segundo)}')
    
def ejercicio_nueve():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    
    full_name = apellido + ', ' + nombre
    
    print(full_name)

def ejercicio_diez():
    palabra = input('Ingrese un texto cualquiera: ')
    
    cantidad = len(palabra)
    
    print(f'La cantidad de letras que tiene la palabra es {cantidad}')
    
def ejercicio_once(): 
    palabra = input('Ingresa un texto cualquiera: ')
    
    primeros_cinco = palabra[:5]
    
    print(f'Los primero cinco caracteres es: {primeros_cinco}')
    
def ejercicio_doce():
    palabra = input('Ingresa un texto que tenga la vocal "a": ')    
    
    nueva_palabra = palabra.replace('a', '')
    
    print(f'El texto sin la letra "a" es: {nueva_palabra}')

def main():
    ejercicio_doce()
    
if __name__ == '__main__':
    main()
