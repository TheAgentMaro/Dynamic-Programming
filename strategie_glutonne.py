
def strategie_gloutonne(n, m, T):
    """
    Implémente la stratégie gloutonne pour déterminer quelle essence d'arbre planter à chaque emplacement
    afin de minimiser le coût total.

    Args:
        n (int): Nombre d'emplacements.
        m (int): Nombre d'essences d'arbres.
        T (List[List[int]]): Matrice de coûts pour planter une essence d'arbre à un emplacement donné.

    Returns:
        Tuple[int, List[int]]: Le coût total de la plantation et la liste des différentes essences utilisées.
    """
    total_cost = 0
    used_essences = []
    last_essence = None

    for i in range(n):
        min_cost = float('inf')
        min_essence = None

        for j in range(m):
            if j != last_essence:
                cost = T[i][j]
                if cost < min_cost:
                    min_cost = cost
                    min_essence = j

        total_cost += min_cost
        used_essences.append(min_essence)
        last_essence = min_essence

    return total_cost, used_essences


# Chargement du fichier tree.txt
with open('tree.txt', 'r') as f:
    values = f.readline().split()
    n = int(values[0])  # Nombre d'emplacements
    m = int(values[1])  # Nombre d'essences
    T = [list(map(int, line.split())) for line in f]


# Application de la stratégie gloutonne
cost, essences = strategie_gloutonne(n, m, T)

# Affichage des résultats
print("Cout total de la plantation :", cost)
print("Essences utilisees (dans l'ordre des emplacements) :", essences)


'''
La stratégie gloutonne ne garantit pas d'obtenir la solution optimale dans tous les cas. 

Exemple : 

T :
	Essence 1	Essence 2
A	    1	      5
B	    5	      1
C	    1	      5


Si nous utilisons la stratégie gloutonne : nous planterions l'essence 1 à A, B et C, ce qui donne un coût total de 7. 

Cependant la solution optimale est de planter l'essence 1 à A et C, et l'essence 2 à B, ce qui donne un coût total de 6.

'''


