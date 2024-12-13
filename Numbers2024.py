#imports
#==================================================================================================
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

#functies
#==================================================================================================
#Vinden convexe veelhoek(en)
def convexe_veelhoek(punten):
    punten = np.array(punten)
    try:
        hull = ConvexHull(punten)
        return hull
    except Exception as e:
        print(f"Fout bij het berekenen van de convex hull: {e}")
        return None

#Punten tekenen + visualizeren veelhoek
def teken_convexe_veelhoek(punten, hull):
    # Teken de wolk van punten
    plt.scatter(punten[:, 0], punten[:, 1], color='blue')
    
    if hull:
        # Teken de convexe veelhoek
        for simplex in hull.simplices:
            plt.plot(punten[simplex, 0], punten[simplex, 1], 'r-', lw=2)

    plt.show()

#wolken definieren
#==================================================================================================
wolken = [
    [(0, 0), (1, 2), (2, 3), (3, 1), (1, 0), (2, 1)],
    [(5, 5), (7, 8), (8, 7), (6, 6)],
    [(10, 10), (11, 13), (12, 15), (14, 14), (12, 10), (13, 12)]
]

#Loop voor berekeningen te doen
#==================================================================================================
for i, wolk in enumerate(wolken):
    print(f"Convexe veelhoek voor wolk {i+1}:")
    hull = convexe_veelhoek(wolk)
    if hull:
        print(f"Vertices van de convex hull: {hull.vertices}")
        # Print de coördinaten van de convex hull
        print(f"Coördinaten van de convex hull: {[wolken[i][j] for j in hull.vertices]}")
        teken_convexe_veelhoek(np.array(wolk), hull)
    else:
        print("Geen convexe veelhoek gevonden.")
