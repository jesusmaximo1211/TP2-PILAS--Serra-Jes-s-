#16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire 
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

#1: definir la clase pila
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
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __str__(self):
        return str(self.elementos)

# Función para encontrar la intersección de dos pilas
def interseccion_pilas(pila1, pila2):
    # Convertir las pilas en conjuntos
    conjunto1 = set()
    conjunto2 = set()

    # Desapilar todos los elementos de la primera pila y agregarlos al conjunto1
    while not pila1.esta_vacia():
        conjunto1.add(pila1.desapilar())

    # Desapilar todos los elementos de la segunda pila y agregarlos al conjunto2
    while not pila2.esta_vacia():
        conjunto2.add(pila2.desapilar())

    # Encontrar la intersección de los dos conjuntos
    interseccion = conjunto1.intersection(conjunto2)

    return list(interseccion)

# Ejemplo de uso
pila_ep_v = Pila()
pila_ep_vii = Pila()

personajes_ep_v = ["Luke Skywalker", "Han Solo", "Leia Organa", "Darth Vader", "Yoda"]
personajes_ep_vii = ["Han Solo", "Leia Organa", "Kylo Ren", "Rey", "Finn", "Luke Skywalker"]

for personaje in personajes_ep_v:
    pila_ep_v.apilar(personaje)

for personaje in personajes_ep_vii:
    pila_ep_vii.apilar(personaje)

result = interseccion_pilas(pila_ep_v, pila_ep_vii)
print("Personajes que aparecen en ambos episodios:", result)