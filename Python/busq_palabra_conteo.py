# Cuenta cuántas veces aparece una palabra en un archivo de texto.
# Uso: python busq_palabra_conteo.py <archivo> <palabra>
# Salida: palabra: número

import sys

# Signos de puntuación que pueden quedar pegados a las palabras
SIGNOS = '.,;:¿?¡!"“”«»()—-'


def leer_archivo(nombre_archivo):
    # Abre el archivo y devuelve su contenido como texto
    with open(nombre_archivo, encoding="utf-8") as archivo:
        return archivo.read()


def contar_palabra(texto, palabra):
    # Minúsculas para que no influyan las mayúsculas
    palabra_buscada = palabra.lower()

    # Lista con todas las palabras del texto
    palabras = texto.lower().split()

    # Recorre la lista y cuenta las coincidencias
    contador = 0
    for p in palabras:
        # Quita los signos de los extremos antes de comparar
        if p.strip(SIGNOS) == palabra_buscada:
            contador += 1
    return contador


def main():
    # DATOS DE ENTRADA
    # Comprueba que se han pasado el archivo y la palabra
    if len(sys.argv) != 3:
        print("Uso: python busq_palabra_conteo.py <archivo> <palabra>")
        return

    nombre_archivo = sys.argv[1]
    palabra = sys.argv[2]

    # PROCESO
    # Lee el archivo y avisa si no existe
    try:
        texto = leer_archivo(nombre_archivo)
    except FileNotFoundError:
        print(f"No se encuentra el archivo: {nombre_archivo}")
        return

    contador = contar_palabra(texto, palabra)

    # SALIDA
    print(f"{palabra}: {contador}")


# Ejecuta main() solo si el script se lanza directamente
if __name__ == "__main__":
    main()