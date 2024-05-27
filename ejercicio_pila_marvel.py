#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. terminar en qué posición se encuentran Rocket Raccoon y Groot, tomando comode posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G

class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_peliculas} películas)"

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def __str__(self):
        return str([str(e) for e in self.elementos])

def posicion_personaje(pila, nombre_personaje):
    temp_pila = Pila()
    posicion = 1
    encontrado = False

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        temp_pila.apilar(personaje)
        if personaje.nombre == nombre_personaje:
            encontrado = True
            break
        posicion += 1

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    return posicion if encontrado else -1

# Ejemplo de uso
pila_mcu = Pila()
personajes = [
    Personaje("Iron Man", 10), Personaje("Captain America", 9), Personaje("Thor", 8),
    Personaje("Black Widow", 7), Personaje("Hulk", 6), Personaje("Hawkeye", 5),
    Personaje("Rocket Raccoon", 4), Personaje("Groot", 3), Personaje("Spider-Man", 3)
]

for personaje in personajes:
    pila_mcu.apilar(personaje)

pos_rocket = posicion_personaje(pila_mcu, "Rocket Raccoon")
pos_groot = posicion_personaje(pila_mcu, "Groot")

print(f"Rocket Raccoon está en la posición: {pos_rocket}")
print(f"Groot está en la posición: {pos_groot}")


def personajes_mas_de_5_peliculas(pila):
    temp_pila = Pila()
    personajes = []

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        temp_pila.apilar(personaje)
        if personaje.cantidad_peliculas > 5:
            personajes.append((personaje.nombre, personaje.cantidad_peliculas))

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    return personajes

# Ejemplo de uso
personajes_mas_5 = personajes_mas_de_5_peliculas(pila_mcu)
print("Personajes que participaron en más de 5 películas:")
for nombre, cantidad in personajes_mas_5:
    print(f"{nombre}: {cantidad} películas")

def cantidad_peliculas_viuda_negra(pila):
    temp_pila = Pila()
    cantidad_peliculas = 0

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        temp_pila.apilar(personaje)
        if personaje.nombre == "Black Widow":
            cantidad_peliculas = personaje.cantidad_peliculas

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    return cantidad_peliculas

# Ejemplo de uso
cantidad_black_widow = cantidad_peliculas_viuda_negra(pila_mcu)
print(f"Black Widow participó en: {cantidad_black_widow} películas")

def personajes_con_letras(pila, letras):
    temp_pila = Pila()
    personajes = []

    while not pila.esta_vacia():
        personaje = pila.desapilar()
        temp_pila.apilar(personaje)
        if personaje.nombre[0] in letras:
            personajes.append(personaje.nombre)

    while not temp_pila.esta_vacia():
        pila.apilar(temp_pila.desapilar())

    return personajes

# Ejemplo de uso
letras = ['C', 'D', 'G']
personajes_letras = personajes_con_letras(pila_mcu, letras)
print("Personajes cuyos nombres empiezan con C, D o G:")
for nombre in personajes_letras:
    print(nombre)

