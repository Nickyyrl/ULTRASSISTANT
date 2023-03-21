import difflib
import random
import time
import os


class Produits:

  def __init__(self):
    self.produits = {
      'Plateforme individuelle legeres roulante':
      'PAM',
      'Equipement de mise en rayon':
      'PICKLY',
      'Materiel reglable a marches pour utilisation sous skydome':
      'MAD SKYDOME',
      'Quai acces arriere camion':
      'ASCAAM',
      'Quai modulaire retractable':
      'QMC',
      'Plateforme pour acces benne a dechet':
      'PFDC',
      'Plateforme individuelle roulante pliante (PIRL)':
      'PIRL',
      'Plateforme individuelle roulante pliante (PIRL) avec stabilisateur':
      'PIRL SD',
      'Plateforme individuelle roulante pliante (PIRL) avec portillon saloon':
      'PIRL SALOON',
      'Plateforme individuelle roulante pliante reglable (PIRC)':
      'PIRC',
      'Plateforme individuelle roulante pliante reglable (PIRC) avec stabilisateur':
      'PIRC SD',
      'PIRL':
      'Plateforme individuelle roulante pliante (PIRL)',
      'PIRL Saloon':
      'Plateforme individuelle roulante pliante (PIRL) avec portillon saloon',
      'PIRL SD':
      'Plateforme individuelle roulante pliante (PIRL) avec stabilisateur',
      'PIRC':
      'Plateforme individuelle roulante pliante reglable (PIRC)',
      'PIRC SD':
      'Plateforme individuelle roulante pliante reglable (PIRC) avec stabilisateur',
      'Echafaudage roulant pour usage intensif':
      'ECOPRO',
      'Echafaudage roulant pliant':
      'PROPLI',
      'Echafaudage valise individuel roulant':
      'M-MAX',
      'Passerelle roulante pour passage au dessus de la sellette arriere cabine camion':
      'EC CAMION',
      'Plateforme roulante modulable':
      'PTF',
      'Materiel acces fond de fouille':
      'MAD FF',
      'Plateforme roulante reglable':
      'EASYTOP',
      'Escabeaux avec sortie lateral pour acces bungalow':
      'ER SL',
      'Escabeaux de rayonnage':
      'ER R',
      'Acces premur':
      'ECPA',
      'Materiel acces dalle reglable':
      'MAD P',
      'Materiel acces dalle reglable avec marche':
      'MAD SP',
      'Plateforme de fixation sur blindage':
      'PF BLIND',
      'Passerelle de franchissement avec caillebotis acier':
      'PLFF',
      'Saut de loup pour acces temporaire et definitif':
      'SAUT DE LOUP',
      'Escabeau de ragreage':
      'PIR ER',
      'Plateforme individuelle roulante double acces':
      'PIR PDA',
      'Plateforme de ragreage double acces':
      'PIR PRDA',
      'Plateforme pour escalier':
      'PFE OU PFEC',
      'Echafaudage roulant pour travaux entretien':
      'TOPLIGHT',
      'Tour grande largeur pour usage intensif':
      'TLS',
      'Plateforme roulante avec echelle pour usage intensif':
      'PAP',
      'Echafaudage escalier tournant':
      'ESCALUTOP',
      'Echelle a crinoline':
      'CS',
      'Echelle simple':
      'SE',
      'Echelle a marches':
      'SME',
      'Quai de dechargement camion':
      'PFDC',
    }

  def chercher_produit(self, entree_utilisateur):
    produit = None
    score = 0
    for k in self.produits.keys():
      s = difflib.SequenceMatcher(None, entree_utilisateur.lower(), k.lower())
      if s.ratio() > score:
        produit = k
        score = s.ratio()
    return produit, self.produits[produit] if produit is not None else None


class ULTRALU:

  def __init__(self, produits):
    self.demande = ""
    self.produits = produits

    self.reponses_positives = [
      "Voici les détails du produit que vous cherchez :",
      "Voila un produit qui pourrait correspondre a votre demande :",
      "Je vous propose :"
    ]

    self.reponses_negatives = [
      "Je suis désolé, je n'ai pas pu trouver de produit correspondant à votre demande.",
      "Je ne peux pas répondre à cette demande. Veuillez réessayer avec une autre demande.",
      "Je ne trouve aucun produit qui corresponde à cette demande. Essayez une nouvelle demande."
    ]

  def repondre_demande(self):
    produit, description = self.produits.chercher_produit(self.demande)
    if produit is not None:
      print("\n" + random.choice(self.reponses_positives) + "\n")
      print(description + " : " + produit)
      return description, produit
    else:
      print(random.choice(self.reponses_negatives))

  def feedback(self):
    satisfaction = str(
      input(
        "[ULTRASSISTANT] : Cette réponse vous a-t-elle aidé ? (oui/non) \n >>> "
      ))
    if satisfaction.lower() == "oui":
      continuer = str(
        input(
          "[ULTRASSISTANT] : Souhaitez-vous chercher un autre produit ? (oui/non) \n >>>"
        )).lower()
      if continuer == "oui":
        time.sleep(1)
        self.bis()
      elif continuer == "non":
        print("[ULTRASSISTANT] : Merci pour votre visite sur Ultralu.com !")
        time.sleep(2)
    else:
      produits_similaires = []
      for produit, description in self.produits.produits.items():
        s = difflib.SequenceMatcher(None, self.demande.lower(),
                                    produit.lower())
        if s.ratio() > 0.27 and produit not in produits_similaires:
          produits_similaires.append(produit)

      if len(produits_similaires) > 0:
        print("\n [ULTRASSISTANT] : Voici quelques produits similaires :")
        for produit in produits_similaires[:5]:
          print(" - {} : {}".format(produit, self.produits.produits[produit]))
      else:
        print(
          "[ULTRASSISTANT] : Je suis désolé, je n'ai pas pu trouver de produits similaires."
        )
        time.sleep(2)
      self.bis()
    

  def salutation(self):
    os.system("cls")
    self.easter_egg()

    print("\n")
    print(
      "[ULTRASSISTANT] : Bonjour, je suis ULTRASSISTANT, votre assistant en ligne pour les produits d'accès en hauteur."
    )
    self.demande = input(
      "\n [ULTRASSISTANT] : Je peux vous aider a trouver un produit si vous me decrivez simplement ce que vous cherchez. \n >>>"
    )
    self.repondre_demande()
    time.sleep(3)
    self.feedback()

  def bis(self):
    self.demande = input(
      "\n[ULTRASSISTANT] : Quel produit souhaitez-vous chercher maintenant ? \n >>>"
    )
    self.repondre_demande()
    time.sleep(3)
    self.feedback()

  def easter_egg(self):
    infos = [
      "ULTRALU a été crée en 1972",
      "Mme Simonin est chez ULTRALU depuis 37 ans ! 37 ans de machines a calculer avec rouleau de papier.",
      "Avant mon nom (CarinALU) etait inspirée de celui de Carine, en l'hommage de notre assisstante commerciale ",
      "VOILAAAAAAAAAAAAA QUOI.",
      "Ils ne savaient que c'etait impossible alors ils l'ont fait, Sylvain VETROFF",
      "Quand on annonce un grand Schlem on fait le grand Schlem, Sylvain VETROFF",
    ]
    print("Chargement en cours... {}".format(random.choice(infos)))
    for i in range(20):
      print("[" + "#" * i + " " * (20 - i) + "]", end="\r")
      time.sleep(0.3)


produits = Produits()
chatbot = ULTRALU(produits)

