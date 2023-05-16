def min_cost_top_down(T, n, m, i=1, prec_tree=None, memo={}):
    """
    Calcule le coût minimal de la plantation d'arbres sur n emplacements,
    en utilisant m essences différentes, en se basant sur une approche dynamique top-down.
    
    
    T : tableau de taille n x m contenant le coût de plantation de chaque essence
    n : nombre d'emplacements
    m : nombre d'essences
    i : emplacement courant
    prec_tree : essence plantée à l'emplacement i-1 (None si aucun arbre planté)
    memo : dictionnaire pour stocker les résultats déjà calculés
    
    """
    if i > n:
        return 0
    
    if (i, prec_tree) in memo:
        return memo[(i, prec_tree)]
    
    min_cost = float('inf')
    
    for j in range(m):
        if prec_tree is not None and prec_tree == j:
            continue
        
        cost = T[i-1][j] + min_cost_top_down(T, n, m, i+1, j, memo)
        
        if cost < min_cost:
            min_cost = cost
    
    memo[(i, prec_tree)] = min_cost
    return min_cost


# Chargement du fichier tree.txt
with open('tree.txt', 'r') as f:
    values = f.readline().split()
    n = int(values[0])  # Nombre d'emplacements
    m = int(values[1])  # Nombre d'essences
    T = [list(map(int, line.split())) for line in f]

cost = min_cost_top_down(T, n, m)

print("Cout minimal de la plantation :", cost)