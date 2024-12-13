#Imports
#==================================================================================================
import tkinter as tk                #(GUI)
from itertools import combinations  #(checken van punten)

#functies
#==================================================================================================
#check voor collineaire punten
def is_collinear(p1, p2, p3):
    """Controleer of drie punten collineair zijn."""
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p2[0] - p1[0]) * (p3[1] - p2[1])

#check voor convexe veelhoek
def is_convex(points):
    """Controleer of een set punten een convexe veelhoek vormt."""
    n = len(points)
    if n < 3:
        return False

    def orientation(p, q, r):
        # Kruisproduct om de oriëntatie te bepalen
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        return val > 0  # True betekent tegen de klok in

    first_orientation = orientation(points[-1], points[0], points[1])
    for i in range(1, n):
        if orientation(points[i - 1], points[i], points[(i + 1) % n]) != first_orientation:
            return False
    return True

#class (convex polygon checker)
#==================================================================================================
class ConvexPolygonChecker:
    #constructor
    #______________________________________________________________________________________________
    def __init__(self, n):
        self.n = n  # Het aantal hoeken dat een convexe veelhoek moet hebben
        self.points = []  # Lijst van geplaatste punten
        self.found_polygon = False  # Of een convexe veelhoek is gevonden
        self.root = tk.Tk()
        self.root.title("Convexe Hoek Checker")
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.canvas.pack()

        # Klikgebeurtenis koppelen
        self.canvas.bind("<Button-1>", self.add_point)

    #functies
    #______________________________________________________________________________________________
    #Voeg een punt toe bij een muisklik
    def add_point(self, event):
        """Voeg een punt toe bij een muisklik."""
        if self.found_polygon:
            return  # Geen nieuwe punten toevoegen als een convexe veelhoek is gevonden

        x, y = event.x, event.y

        # Controleer collineariteit
        for p1, p2 in combinations(self.points, 2):
            if is_collinear(p1, p2, (x, y)):
                print("Punt mag niet collineair zijn met bestaande punten.")
                return

        # Teken het punt
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

        # Controleer op convexe veelhoek
        if len(self.points) >= self.n:
            for subset in combinations(self.points, self.n):
                if is_convex(subset):
                    self.draw_polygon(subset)
                    print("Convexe veelhoek gevonden!")
                    print("Coördinaten van de veelhoek:")
                    for point in subset:
                        print(f"({point[0]}, {point[1]})")
                    self.found_polygon = True  # Blokkeer verdere invoer
                    return

    #Teken een polygon op het canvas
    def draw_polygon(self, points):
        """Teken een polygon op het canvas."""
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    #Start de Tkinter-hoofdloop
    def run(self):
        """Start de Tkinter-hoofdloop."""
        self.root.mainloop()

#main
#==================================================================================================
if __name__ == "__main__":
    n = int(input("Geef het aantal hoeken N: "))
    app = ConvexPolygonChecker(n)
    app.run()