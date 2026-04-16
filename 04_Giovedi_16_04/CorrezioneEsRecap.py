import random


# =========================
# FUNZIONI
# =========================

def chiedi_numero_positivo():
    """Punto 1: chiede un numero intero positivo finché non è valido."""
    while True:
        try:
            n = int(input("Inserisci un numero intero positivo: "))
            if n > 0:
                return n
            else:
                print("Errore: il numero deve essere maggiore di zero.")
        except ValueError:
            print("Errore: devi inserire un numero intero.")


def genera_lista_casuale(n):
    """Punto 2: genera una lista di lunghezza n con valori casuali tra 1 e n."""
    lista = []
    for _ in range(n):
        lista.append(random.randint(1, n))
    return lista


def somma_numeri_pari(lista):
    """Punto 3: calcola e restituisce la somma dei numeri pari della lista."""
    somma = 0
    for numero in lista:
        if numero % 2 == 0:
            somma += numero
    return somma


def stampa_numeri_dispari(lista):
    """Punto 4: stampa tutti i numeri dispari della lista."""
    print("Numeri dispari nella lista:")
    for numero in lista:
        if numero % 2 != 0:
            print(numero, end=" ")
    print()


def e_primo(numero):
    """Punto 5: restituisce True se il numero è primo, altrimenti False."""
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True


def stampa_numeri_primi(lista):
    """Punto 6: stampa tutti i numeri primi presenti nella lista."""
    print("Numeri primi nella lista:")
    for numero in lista:
        if e_primo(numero):
            print(numero, end=" ")
    print()


def verifica_somma_prima(lista):
    """Punto 7: verifica se la somma di tutti i numeri della lista è un numero primo."""
    somma = 0
    for numero in lista:
        somma += numero

    print(f"Somma totale della lista: {somma}")

    if e_primo(somma):
        print("La somma è un numero primo.")
    else:
        print("La somma NON è un numero primo.")


def mostra_menu():
    print("\n===== MENU =====")
    print("1. Inserisci n")
    print("2. Genera lista casuale")
    print("3. Somma dei numeri pari")
    print("4. Stampa numeri dispari")
    print("5. Verifica se un numero è primo")
    print("6. Stampa numeri primi della lista")
    print("7. Verifica se la somma della lista è un numero primo")
    print("8. Mostra lista")
    print("0. Esci")


# =========================
# MAIN
# =========================

def main():
    n = None
    lista = []

    while True:
        mostra_menu()

        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                n = chiedi_numero_positivo()
                print(f"Hai inserito n = {n}")

            case "2":
                if n is None:
                    print("Devi prima inserire n con il punto 1.")
                else:
                    lista = genera_lista_casuale(n)
                    print("Lista generata correttamente.")
                    print("Lista:", lista)

            case "3":
                if not lista:
                    print("Devi prima generare la lista con il punto 2.")
                else:
                    risultato = somma_numeri_pari(lista)
                    print(f"Somma dei numeri pari: {risultato}")

            case "4":
                if not lista:
                    print("Devi prima generare la lista con il punto 2.")
                else:
                    stampa_numeri_dispari(lista)

            case "5":
                try:
                    numero = int(input("Inserisci un numero da verificare: "))
                    if e_primo(numero):
                        print(f"{numero} è un numero primo.")
                    else:
                        print(f"{numero} NON è un numero primo.")
                except ValueError:
                    print("Errore: devi inserire un numero intero.")

            case "6":
                if not lista:
                    print("Devi prima generare la lista con il punto 2.")
                else:
                    stampa_numeri_primi(lista)

            case "7":
                if not lista:
                    print("Devi prima generare la lista con il punto 2.")
                else:
                    verifica_somma_prima(lista)

            case "8":
                if not lista:
                    print("La lista non è stata ancora generata.")
                else:
                    print("Lista corrente:", lista)

            case "0":
                print("Programma terminato.")
                break

            case _:
                print("Scelta non valida. Riprova.")


main()
