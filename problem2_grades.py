# Liste des etudiant avec leur note 
students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Baraïna", 7)
]
# Fonction pour afficher chaque etudiant avec sa note 
def afficher_notes():
    for name, grade in students:
        print(f"{name} : {grade}")
#fonction pour calculer et afficher les statistique de la classe
def calcul_statistiques():
    notes = [grade for _, grade in students]
    print("Moyenne de la classe :", sum(notes) / len(notes))
    print("Note maximale :", max(notes))
    print("Note minimale :", min(notes))
# Fontion pour afficherles liste des admis  et ajourner 
def afficher_listes():
    admis = [name for name, grade in students if grade >= 10]
    ajournes = [name for name, grade in students if grade < 10]
    print("Étudiants admis :", admis)
    print("Étudiants ajournés :", ajournes)

# Exécution du programme 
afficher_notes()
calcul_statistiques()
afficher_listes()
