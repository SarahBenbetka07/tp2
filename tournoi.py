# tournoi.py

from joueur import Joueur
from match import Match
import utils

class Tournoi:
    def __init__(self, nom):
        """
        Initialise un tournoi avec son nom.
        Initialise aussi une liste vide pour les joueurs et pour les matchs.
        """
        self.nom = nom
        self.joueurs = []
        self.matchs = []

    def charger_joueurs(self, chemin_csv):
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo = ligne[0]
            joueur = Joueur(pseudo)
            self.joueurs.append(joueur)
        """
        Lire un fichier CSV contenant les joueurs.
        Chaque ligne contient un pseudonyme.
        Pour chaque ligne, créer un objet Joueur et l'ajouter à la liste des joueurs.
        Utiliser la fonction lire_csv() du fichier utils.py.
        """


    def charger_matchs(self, chemin_csv):
        """
        Lire un fichier CSV contenant les matchs.
        Chaque ligne contient deux pseudos de joueurs (joueur1, joueur2).
        Trouver les objets Joueur correspondants dans la liste de joueurs.
        Pour chaque ligne, créer un objet Match et l'ajouter à la liste des matchs.
        Utiliser la fonction lire_csv() du fichier utils.py.
        """
        lignes = utils.lire_csv(chemin_csv)
        for ligne in lignes:
            pseudo1 = ligne[0]
            pseudo2 = ligne[1]

            joueur1 = next((j for j in self.joueurs if j.pseudo == pseudo1), None)
            joueur2 = next((j for j in self.joueurs if j.pseudo == pseudo2), None)

            if joueur1 and joueur2:
                match = Match(joueur1, joueur2)
                self.matchs.append(match)
        

    def saisir_scores(self):
        """
        Pour chaque match dans la liste des matchs :
        - Afficher le match (afficher les pseudos des deux joueurs)
        - Demander à l'utilisateur d'entrer les deux scores (score du joueur 1, score du joueur 2)
        - Enregistrer les scores dans l'objet Match
        - Déterminer le gagnant du match
        - Si un gagnant existe (pas d'égalité), appeler enregistrer_victoire() sur le joueur gagnant.
        """
    
        # Match 1
    print("Match 1 : PlayerOne vs PlayerTwo")
    score1 = input("Score de PlayerOne : ")
    score2 = input("Score de PlayerTwo : ")
    if score1.isdigit() and score2.isdigit():
       score1 = int(score1)
       score2 = int(score2)
       if score1 > score2:
         print("PlayerOne gagne.")
       elif score2 > score1:
         print("PlayerTwo gagne.")
       else:
         print("Égalité.")
    else:
      print("Les scores doivent être des nombres.")

# Match 2
    print("Match 2 : PlayerThree vs PlayerFour")
    score1 = input("Score de PlayerThree : ")
    score2 = input("Score de PlayerFour : ")
    if score1.isdigit() and score2.isdigit():
      score1 = int(score1)
      score2 = int(score2)
      if score1 > score2:
         print("PlayerThree gagne.")
      elif score2 > score1:
        print("PlayerFour gagne.")
      else:
        print("Égalité.")
    else:
     print("Les scores doivent être des nombres.")

# Match 3
    print("Match 3 : PlayerOne vs PlayerThree")
    score1 = input("Score de PlayerOne : ")
    score2 = input("Score de PlayerThree : ")
    if score1.isdigit() and score2.isdigit():
     score1 = int(score1)
     score2 = int(score2)
     if score1 > score2:
        print("PlayerOne gagne.")
     elif score2 > score1:
        print("PlayerThree gagne.")
     else:
        print("Égalité.")
    else:
     print("Les scores doivent être des nombres.")

# Match 4
    print("Match 4 : PlayerTwo vs PlayerFour")
    score1 = input("Score de PlayerTwo : ")
    score2 = input("Score de PlayerFour : ")
    if score1.isdigit() and score2.isdigit():
     score1 = int(score1)
     score2 = int(score2)
     if score1 > score2:
        print("PlayerTwo gagne.")
     elif score2 > score1:
        print("PlayerFour gagne.")
     else:
        print("Égalité.")
    else:
      print("Les scores doivent être des nombres.")

    

    def afficher_classement(self):
        """
        Afficher le classement des joueurs.
        Classer les joueurs du plus grand nombre de victoires au plus petit.
        Afficher leur pseudo et leur nombre de victoires.
        """
        self.joueurs.sort(key=lambda j: j.victoires, reverse=True)
        print("Classement des joueurs :")
        for joueur in self.joueurs:
            print(f"{joueur.pseudo} - Victoires : {joueur.victoires}")

    def sauvegarder(self, chemin_json):
        """
        Sauvegarder le tournoi dans un fichier JSON.
        Le fichier doit contenir :
        - le nom du tournoi
        - la liste des joueurs (convertis en dictionnaires à l'aide de la fonction to_dict déjà implémenté dans la classe Joueur)
        Utiliser la fonction sauvegarder_json() du fichier utils.py.
        """
        donnees = { "nom": self.nom, "joueurs": [j.to_dict() for j in self.joueurs] }
        utils.sauvegarder_json(donnees, chemin_json)
        print(f"Tournoi sauvegardé dans {chemin_json}")

    def generer_rapport(self, chemin_text):
        contenu = f"Tournoi : {self.nom}\n\n"
        """
        Générer un rapport du tournoi sous forme de fichier texte.
        Le rapport doit contenir :
        - Le nom du tournoi
        - La liste des matchs joués avec leurs scores
        - Le classement final
        Utiliser la fonction ecrire_texte() du fichier utils.py.
        """
    
        contenu += "Matchs joués :\n"
        for match in self.matchs:
            contenu += f"{match.joueur1.pseudo} {match.score1} - {match.score2} {match.joueur2.pseudo}\n"

        contenu += "\nClassement final :\n"
        joueurs_tries = sorted(self.joueurs, key=lambda j: j.victoires, reverse=True)
        for joueur in joueurs_tries:
            contenu += f"{joueur.pseudo} : {joueur.victoires} victoires\n"

        utils.ecrire_texte(contenu, chemin_text)
