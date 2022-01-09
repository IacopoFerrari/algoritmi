"""
TESTO PROBLEMA:
Questo programma attraverso l'utilizzo di una funzione ricorsiva semplifica un grafo delle precedenze.
I grafi delle precedenze sono grafi che rappresentano l'evoluzione di un processo.
Sono grafi orientati che rappresentano l'evoluzione di un sistema in cui sono presenti più processi che hanno reciproche
dipendenze di sequenzialità. I processi sono rappresentati dai nodi e le precedenze sono rappresentate dagli archi.
In presenza di precedenze implicite queste si possono semplificare in quanto risultano ridondanti
Nel codice il grafo è modellato attraverso un dizionario le cui chiavi indicano i nodi e i valori contenuti in una
lista sono i nodi che sono raggiunti (direttamente e non direttamente) da quel nodo.
Il grafo è prodotto in modo randomico.
"""
import random
numero_processi = 16
dizionario_precedenze= {}

def crea_grafo_precedenze_random(numero_processi):
    for processo in range(numero_processi):
        dizionario_precedenze[processo] = [random.randint(0,processo-1) for x in range(0,random.randint(0,processo))]
        dizionario_precedenze[processo].sort()
        dizionario_precedenze[processo] = list(set(dizionario_precedenze[processo]))

    return dizionario_precedenze

def crea_listone_prec(dizionario_precedenze, precedenze, listoneprec=[]):
    if precedenze:
        for j in precedenze:
            if dizionario_precedenze[j]:
                listoneprec.append(dizionario_precedenze[j])

            # una funzione che richiama se stessa!! ricorsione
            listoneprec = crea_listone_prec(dizionario_precedenze, dizionario_precedenze[j], listoneprec)
    else:
        return listoneprec

    return listoneprec

if __name__ == "__main__":
    dizionario_precedenze = crea_grafo_precedenze_random(numero_processi)
    #esempio di dizionario_precedenze = {0: [], 1: [0], 2: [0,1], 3: [1], 4: [1, 2, 3], 5: [0, 1, 2, 4]}
    print("grafo iniziale: ", dizionario_precedenze)
    dizionario_precedenze_sempl = dizionario_precedenze.copy()
    for processo in range(numero_processi):
        listoneprec = crea_listone_prec(dizionario_precedenze, dizionario_precedenze[numero_processi - processo - 1], [])
    #    print(listoneprec)
        for liste in listoneprec:
            for elem in liste:
                if elem in dizionario_precedenze[numero_processi - processo - 1]:
                    dizionario_precedenze_sempl[numero_processi - processo - 1].remove(elem)

    print("grafo semplificato", dizionario_precedenze_sempl)