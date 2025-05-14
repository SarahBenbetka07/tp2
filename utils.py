# utils.py

import csv
import json

def lire_csv(chemin):
    """
    Lire un fichier CSV et retourner la liste des lignes.
    Chaque dictionnaire correspond à une ligne du fichier.
    """
    lignes = []
    with open(chemin, newline='', encoding='utf-8') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            lignes.append(ligne)
    return lignes

def sauvegarder_json(data, chemin):
    """
    Sauvegarder des données dans un fichier JSON.
    - data : un objet Python (par exemple, un dictionnaire ou une liste)
    - chemin : chemin du fichier JSON à écrire
    Utiliser json.dump avec indentation pour que le fichier soit lisible.
    """
    with open(chemin, 'w', encoding='utf-8') as fichier_json:
        json.dump(data, fichier_json, indent=4, ensure_ascii=False)

def ecrire_texte(contenu, chemin):
    """
    Écrire du texte brut dans un fichier texte (.txt).
    - contenu : texte à écrire
    - chemin : chemin du fichier texte à créer
    """
    with open(chemin, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)
