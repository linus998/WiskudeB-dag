# Wiskunde B-dag 2024

Dit project bevat een verzameling programma's en een Excel-bestand, gemaakt tijdens de Wiskunde B-dag 2024. De tools helpen bij het analyseren en visualiseren van veelhoeken in puntenwolken.

## Inhoud van de bestanden

### **1. Game2024.py**
- **Doel**: Applicatie waarmee je punten kunnen toevoegen via een GUI tot die punten een veelhoek vormen.
- **Belangrijkste functionaliteiten**:
  - Controle op collineaire punten.
  - Detectie en visualisatie van een veelhoek.
  - Gebouwd met Tkinter voor de gebruikersinterface.

---

### **2. Numbers2024.py**
- **Doel**: Meerdere puntenwolken analyseren en visualiseren (voor convexe veelhoeken).
- **Belangrijkste functionaliteiten**:
  - Detecteert convexe veelhoeken in vooraf ingegeven puntenwolken.
  - Gebruikt de `scipy.spatial.ConvexHull`-bibliotheek.
  - Toont resultaten in grafieken.
- **Uitvoering**:
  Het script bevat een reeks vooraf ingetypte wolken. Bij uitvoering worden de resultaten van elke wolk gechecked en getoond.

---

### **3. Testen2024.py**
- **Doel**: Controleert of een gegeven veelhoek convex is.
- **Belangrijkste functionaliteiten**:
  - Bevat een hoofdfunctie `is_convex_polygon` die een lijst van coördinaten analyseert.
- **Uitvoering**:
  Voer het script uit om ingebouwde voorbeelden te testen.

---

### **4. random_punten.xlsx**
- **Doel**: Bevat een gegenereerde lijst van puntenwolken. Deze wolken kunnen worden gebruikt als invoer om de scripts te testen.

---

## Auteurs
Onze groep:
- Linus Beheydt
- Mats Verschoren
- Xenne Delanghe
- Mathias Nickmans
