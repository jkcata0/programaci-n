def validar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número positivo (o 'S' para terminar): "))
            if numero <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                return numero
        except ValueError:
            entrada = input("Entrada no válida. ¿Desea salir? (S/N): ")
            if entrada.upper() == 'S':
                return None
            else:
                print("Por favor, ingrese un número entero positivo.")

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def determinar_primos(lista_numeros):
    resultados = {}
    for numero in lista_numeros:
        resultados[numero] = es_primo(numero)
    return resultados

def main():
    numeros = []
    while True:
        numero = validar_numero()
        if numero is None:
            break
        numeros.append(numero)

    resultados_primos = determinar_primos(numeros)

    print("Salida:")
    for numero, es_primo_resultado in resultados_primos.items():
        print(f"{numero}: {es_primo_resultado}")

if __name__ == "__main__":
    main()
