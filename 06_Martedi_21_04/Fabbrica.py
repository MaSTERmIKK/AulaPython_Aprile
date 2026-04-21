import Automobile as Auto

def crea_auto(marca: str, modello: str):
    auto = Auto.Automobile(marca, modello)
    auto.stampa_info()
    return auto

def main():
    lista_auto = []

    while True:
        marca = input("Inserisci la marca (Q per uscire): ")
        if marca.lower() == "q":
            break

        modello = input("Inserisci il modello: ")
        lista_auto.append(crea_auto(marca, modello))

    print(f"\nAuto in lista: {len(lista_auto)}")
    for auto in lista_auto:
        auto.stampa_info()

main()
