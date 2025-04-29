from random import randint

def ejercicio_uno():
    numeros = []
    
    for i in range(1, 11):
        numeros.append(i)
    
    print(numeros[4])

def ejercicio_dos():
    numeros = []
    
    for i in range(1, 11):
        numeros.append(i)
    print(len(numeros))

def ejercicio_tres():
    numeros = []
    for i in range(0, 10):
        numeros.append(randint(0, 200))
    
    print(f'El número máximo de la lista: {max(numeros)}')
    print(f'El número minimo de la lista: {min(numeros)}')

def ejercicio_cuatro():
    numeros = []
    for i in range(0, 10):
        numeros.append(randint(0, 200))
    
    print(f'Lista de forma original: {numeros}')
    print(f'Lista ordenada: {sorted(numeros)}')

def ejercicio_cinco():
    informacion = ('Sofía', 26)
    
    print(f'La edad de la persona que está dentro de: {informacion[1]} años de edad')
    
def ejercicio_seis():
    # Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
    nombres = ['Sofía', 'Marcelo', 'Lucas', 'Miguel', 'Sol']
    print(f'Lista original: {nombres}')
    
    # a. Cambiar el último elemento de la lista y cambiar el último por "Juan".
    # Sin saber cuantos elementos tiene la lista
    nombres[-1] = 'Juan'
    print(f'Lista alterada: {nombres}')
    
    # b. Devolver el nombre que esta a dos posiciones del final. ¿Cómo hacemos para que nos funcione
    # para cualquier lista y no solo para la que tenga 5 elementos?
    print(nombres[-2])
    
    # c. Recorrer la lista e imprimir cada nombre por pantalla
    for nombre in nombres:
        print(nombre)
    
    # d. Imprimir por pantalla la lista con 3 repeticiones. usar el operador repetición (*)
    for nombre in  nombres:
        print((nombre + ' ') * 3)
    

def ejercicio_siete():
    # Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación
    # guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas por separado?
    sofia = ('Sofía', 25)
    miguel = ('Miguél', 30)
    lucas = ('Lucas', 28)
    nombres = [sofia, miguel, lucas]
    
    # Podemos obtener el nombre y la edad de cada tupla
    for nombre in nombres:
        print(f'Nombre: {nombre[0]}, Edad: {nombre[1]}')

def ejercicio_ocho():
    francia = ('Francia', 'París', 'Europa')
    argentina = ('Argentina', 'Buenos Aires', 'América del sur')
    japon = ('Japón', 'Tokyo', 'Asia')
    peru = ('Perú', 'Lima', 'Améria del sur')
    
    paises = [francia, argentina, japon, peru]
    
    def imprimir_pais(paises):
        for pais in paises:
            print(f'País: {pais[0]}')
            print(f'Capital: {pais[1]}')
            print(f'Contiente: {pais[2]}')
            print()
    
    
    imprimir_pais(paises)

def main():
    ejercicio_ocho()
    
if __name__ == '__main__':
    main()
    