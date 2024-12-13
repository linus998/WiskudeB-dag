#hoofdfunctie
#=================================================================================
def is_convex_polygon(coords):
    #functie voor kruisproducten te berekenen
    def cross_product(p1, p2, p3): return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
   
    n = len(coords)
    if n < 3:
        return False  # Geen veelhoek mogelijk
    
    # Initialiseer oriëntatie
    prev_orientation = None

    for i in range(n):
        p1 = coords[i]
        p2 = coords[(i + 1) % n]  # Volgende punt
        p3 = coords[(i + 2) % n]  # Punt daarna

        # Bereken oriëntatie
        orientation = cross_product(p1, p2, p3)
        
        if orientation != 0:  # Negeer collineaire punten
            if prev_orientation is None:
                prev_orientation = orientation  # Zet initiële oriëntatie
            elif (prev_orientation > 0 and orientation < 0) or (prev_orientation < 0 and orientation > 0):
                return False  # Niet-convex
            prev_orientation = orientation

    return True

#voorbeelgebruiken
#=================================================================================
coordinaten1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
print("Is convexe veelhoek:", is_convex_polygon(coordinaten1))

coordinaten2 = [(56, 377), (152, 360), (279, 356), (350, 391), (34, 26), (156,60), (276,62), (365,28), (224,69), (218, 352), (76,184), (152, 195), (116,189), (41, 168), (23, 171), (10, 169)]
print("Is convexe veelhoek:", is_convex_polygon(coordinaten2))
