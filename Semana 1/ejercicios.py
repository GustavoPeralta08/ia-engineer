#Primer ejercicio
def invertir(texto: str) -> str:
    return texto[::-1]

print(invertir("hola"))

#Segundo ejercicio
def contar_palabras(ruta: str) -> int:
    with open(ruta, encoding="utf-8") as f:
        return len(f.read().split())

print(contar_palabras("texto.txt"))

#tercer ejercicio
numeros = range(1, 21)
pares = [n for n in numeros if n % 2 == 0]
print(pares)

#Cuarto ejercicio
def frecuencia_letras(texto: str) -> dict[str, int]:
    frec = {}
    for c in texto.lower():
        if c.isalpha():
            frec[c] = frec.get(c, 0) + 1
    return frec

print(frecuencia_letras("Hola mundo"))