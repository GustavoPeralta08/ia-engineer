#Primer ejercicio
def invertir(texto: str) -> str:
    return texto[::-1]

print(invertir("hola"))

#Segundo ejercicio
def contar_palabras(ruta: str) -> int:
    with open(ruta, encoding="utf-8") as f:
        return len(f.read().split())

print(contar_palabras("texto.txt"))