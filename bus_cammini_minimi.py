"""TESTO PROBLEMA:
We have a list of bus routes, each routes[i] is a bus route that the i-th bus repeats forever.
For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence
1->5->7->1->5->7->1->.
We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
Travelling by buses only, what is the least number of buses we must take to reach our destination?
Return -1 if it is not possible.
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
"""
#routes esempio
#routes = [[43, 6], [1, 2, 7], [3, 5, 7], [2, 98], [98, 43]]
import random
#routes con 6 linee, fermate da 30 a 36 generate randomicamente
routes = [list(set([random.randint(30,36) for x in range(random.randint(2,4))])) for x in range(0,6)]
print("routes: ", routes)
S = routes[0][0]
T = routes[5][-1]
print("fermata di partenza: ", S)
print("fermata di arrivo: ", T)
sup_cammino = len(routes) + 1
# popolo un dizionario con chiave una linea e valori una lista con le linee con cui è connessa direttamente
dizionario_connessioni = {}
for linea_partenza in range(len(routes)):
    dizionario_connessioni[linea_partenza] = []
    for fermata in routes[linea_partenza]:
        for linea_arrivo in range(len(routes)):
            if fermata in routes[linea_arrivo] and linea_partenza != linea_arrivo and fermata not in \
                    dizionario_connessioni[linea_partenza]:
                dizionario_connessioni[linea_partenza].append(linea_arrivo)

print("dizionario_connessioni: ", dizionario_connessioni)


def trova_cammino(linee_partenza, cammino_minimo=1, linee_visitate=[]):
    cammino_minimo += 1
    print("linee_partenza: ", linee_partenza)
    linee_raggiunte = []
    for linea in linee_partenza:
        linee_visitate.append(linea)
        linee_raggiunte.extend(x for x in dizionario_connessioni[linea] if x not in linee_raggiunte)
        for indice_linea in linee_raggiunte:
            if indice_linea not in linee_visitate:
                if T in routes[indice_linea]:
                    return cammino_minimo

    print("linee_raggiunte: ", linee_raggiunte)
    print("linee_visitate: ", linee_visitate)
    if not [item for item in linee_raggiunte if item not in linee_visitate]:
        return sup_cammino

    else:
        cammino_minimo = trova_cammino(linee_raggiunte, cammino_minimo, linee_visitate) #ricorsione

    return cammino_minimo
################################FINE FUNZIONE#####################

if __name__ == "__main__":
    linee_partenza = []
    for linea in routes:
        for fermata in linea:
            if S == fermata:
                linee_partenza.append(routes.index(linea))

    print("linee in cui trovo la partenza: ", linee_partenza)
    for linee in linee_partenza:
        if T in routes[linee]:
            cammino_minimo = 1
            break

    else:
        cammino_minimo = trova_cammino(linee_partenza)

        if cammino_minimo == len(routes) + 1:
            cammino_minimo = -1 # ritorno -1 se non ho trovato il cammino, come da consegna

    print("cammino_minimo trovato: ", cammino_minimo)