# fonction pour compter les voyelles
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text if char in vowels)
#fonction pour transformer la phrase:
#-mots de longueur paire en majuscules
#-mots de longueur inpaire en minuscule
def transform_phrase(words):
    transformed = []
    for word in words:
        if len(word) % 2 == 0:
            transformed.append(word.upper())
        else:
            transformed.append(word)
    return " ".join(transformed)

# Entrée utilisateur 
phrase = input("Entrez une phrase : ").lower()
words = phrase.split() # Decouper en liste de mots

# Affichages des resultats
print("Nombre total de mots :", len(words))
print("Mot le plus long :", max(words, key=len))
print("Nombre total de voyelles :", count_vowels(phrase))
print("Nouvelle phrase :", transform_phrase(words))

