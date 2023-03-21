import difflib
import random
import time
import os
from difflib import get_close_matches


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

  def feedback(self, demande):
    produits_proches = []
    scores_produits = {}
    for k in self.produits.keys():
        s = difflib.SequenceMatcher(None, demande.lower(), k.lower())
        scores_produits[k] = s.ratio()
    produits_tries = sorted(scores_produits.items(), key=lambda x: x[1], reverse=True)
    for i in range(5):
        if i >= len(produits_tries):
            break
        produits_proches.append(produits_tries[i][0])
    return produits_proches


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
      produits_proches = self.produits.feedback(self.demande) # <-- modifier ici
      return description, produit, produits_proches



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



produits = Produits()
chatbot = ULTRALU(produits)

