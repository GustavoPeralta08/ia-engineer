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

#Quinto ejercicio
def media_y_mediana(nums: list[float]) -> tuple[float, float]:
    if not nums:
        raise ValueError("La lista no puede estar vacía")
    ordenados = sorted(nums)
    n = len(ordenados)
    media = sum(ordenados) / n
    mid = n // 2
    if n % 2:
        mediana = ordenados[mid]
    else:
        mediana = (ordenados[mid - 1] + ordenados[mid]) / 2
    return media, mediana

print(media_y_mediana([3, 1, 4, 1, 5]))  # (2.8, 3)

#Sexto ejercicio
import json

datos = {"nombre": "Ana", "edad": 30, "lenguajes": ["Python", "C#"]}

with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)

with open("datos.json", encoding="utf-8") as f:
    leidos = json.load(f)

print(leidos["nombre"])

#Septimo ejercicio
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad

    def retirar(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

cuenta = CuentaBancaria("Ana", 100)
cuenta.depositar(50)
cuenta.retirar(30)
print(cuenta.saldo)  # 120

#Octavo ejercicio
try:
    with open("no_existe.txt", encoding="utf-8") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")