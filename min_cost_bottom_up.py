def min_cost_bottom_up(T, n, m):
    """
    Calcule le coût minimal de la plantation d'arbres sur n emplacements,
    en utilisant m essences différentes, en se basant sur une approche dynamique bottom-up.
    
    
    T : tableau de taille n x m contenant le coût de plantation de chaque essence
    n : nombre d'emplacements
    m : nombre d'essences
    """
    
    # Créer un tableau pour stocker les coûts optimaux
    cp = [[0] * m for _ in range(n)]
    
    # Remplir le tableau cp de bas en haut en calculant les coûts optimaux
    for i in range(n-1, -1, -1):
        for j in range(m):
            # Cas de base : dernier emplacement
            if i == n-1:
                cp[i][j] = T[i][j]
            else:
                # Calculer le coût de la plantation de l'essence j à l'emplacement i
                # en ajoutant le coût minimal de la plantation sur les emplacements suivants (i+1,...,n)
                min_cost = float('inf')
                for k in range(m):
                    if k != j:
                        cost = T[i][j] + cp[i+1][k]
                        if cost < min_cost:
                            min_cost = cost
                cp[i][j] = min_cost
    
    # Trouver le coût minimal total
    min_cost = float('inf')
    for j in range(m):
        if cp[0][j] < min_cost:
            min_cost = cp[0][j]
    
    # Trouver la liste des essences utilisées
    essences = []
    j = cp[0].index(min_cost)
    essences.append(j+1)  # Ajouter l'essence à la première position
    for i in range(1, n):
        for k in range(m):
            if k != j and cp[i][k] == min_cost - T[i-1][j]:
                essences.append(k+1)  # Ajouter l'essence à la position i
                min_cost -= T[i-1][j]
                j = k
                break
    
    return min_cost, essences

# Chargement du fichier tree.txt
with open('tree.txt', 'r') as f:
    values = f.readline().split()
    n = int(values[0])  # Nombre d'emplacements
    m = int(values[1])  # Nombre d'essences
    T = [list(map(int, line.split())) for line in f]

cost, essences = min_cost_bottom_up(T, n, m)

print("Coût minimal de la plantation :", cost)
print("Liste des essences utilisées :", essences)