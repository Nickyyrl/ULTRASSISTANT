import logging
from flask import Flask, render_template, request, jsonify
from chatbotv7 import Produits, ULTRALU
from user_agents import parse
import os

app = Flask(__name__)
produits = Produits()
assistant = ULTRALU(produits)

# Créer un objet logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Configurer le gestionnaire de logs pour écrire dans un fichier
file_handler = logging.FileHandler('logs.txt')
file_handler.setLevel(logging.INFO)

# Configurer le formatteur pour inclure l'heure, le niveau de log et le message
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Ajouter le gestionnaire de logs à l'objet logger
logger.addHandler(file_handler)

def print_in_box(msg):
    length = len(msg)
    print("+" + "-"*(length+2) + "+")
    print("| " + msg + " |")
    print("+" + "-"*(length+2) + "+")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def demande():
    if not request.form['text']:
        return render_template('index.html')
    assistant.demande = request.form['text']
    description, produit, produits_proches = assistant.repondre_demande()
    reponse = "[ULTRASSISTANT] : Pour votre description, {}, je vous propose : {} | {}".format(assistant.demande, description, produit)

    # Récupérer l'adresse IP et les informations du navigateur et de l'appareil utilisé par l'utilisateur
    user_agent = parse(request.headers.get('User-Agent'))
    ip = request.remote_addr

    # Ajouter une entrée dans les logs
    logger.info('Demande de l\'utilisateur : %s', assistant.demande)
    logger.info('Adresse IP : %s', ip)
    logger.info('Navigateur : %s', user_agent.browser.family)
    logger.info('Appareil : %s', user_agent.device.family)

    print('\n')
    print_in_box("Informations utilisateur:")
    print("Adresse IP:", ip)
    print("Navigateur:", user_agent.browser.family)
    print("Appareil:", user_agent.device.family)
    print_in_box("Réponse:")
    print(reponse)
    print_in_box("Feedback")
    print(feedback)

    return render_template('index.html', reponse=reponse)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    response_id = data['responseId']

    # Si l'utilisateur a mis un dislike, proposer 5 produits les plus proches

    description, produit, produits_proches = assistant.repondre_demande()

        # Retourner une réponse JSON avec les produits proposés
    print(str(produits_proches))
    return jsonify({'produits_proches': produits_proches})



app.run(host='0.0.0.0', port=5000)
