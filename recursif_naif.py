def min_cost_rec(T, n, m, i=1, prec_tree=None):
    """
    Calcule le coût minimal de la plantation d'arbres sur n emplacements,
    en utilisant m essences différentes, en se basant sur un algorithme récursif naïf.
    
    
    T : tableau de taille n x m contenant le coût de plantation de chaque essence
    n : nombre d'emplacements
    m : nombre d'essences
    i : emplacement courant
    
    prec_tree : essence plantée à l'emplacement i-1 (None si aucun arbre planté)
    """
    # Cas de base : on a planté des arbres sur tous les emplacements, on retourne un coût nul
    if i > n:
        return 0
    
    min_cost = float('inf')
    
    # On boucle sur toutes les essences possibles pour l'emplacement courant i
    for j in range(m):
        if prec_tree is not None and prec_tree == j:
            continue
        
        # On calcule le coût de la plantation de l'essence j à l'emplacement i,
        # en ajoutant le coût minimal de la plantation sur les emplacements suivants (i+1,...,n)
        cost = T[i-1][j] + min_cost_rec(T, n, m, i+1, j)
        
        # Si le coût obtenu est inférieur au coût minimal actuel, on le met à jour
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

# Chargement du fichier tree.txt
with open('tree.txt', 'r') as f:
    values = f.readline().split()
    n = int(values[0])  # Nombre d'emplacements
    m = int(values[1])  # Nombre d'essences
    T = [list(map(int, line.split())) for line in f]

cost = min_cost_rec(T, n, m)

print("Coût minimal de la plantation :", cost)