from flask import Flask, render_template, request
from chatbotv7 import Produits, ULTRALU
import os

app = Flask(__name__)   
produits = Produits()
assistant = ULTRALU(produits)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/', methods=['POST'])
def demande():
    if not request.form['text']:
        return render_template('index.html')
    assistant.demande = request.form['text']
    description, produit = assistant.repondre_demande()
    reponse = "[ULTRASSISTANT] : Pour votre description {} je vous propose : {} | {}".format(assistant.demande, description, produit)
    print("Demande de l'utilisateur : ", assistant.demande)
    print("Reponse : {} - {} ".format(produit, description))
        # Récupérer l'adresse IP du client
    ip = request.remote_addr

        # Récupérer le lieu à partir de l'adresse IP
        # Cette étape peut nécessiter une API tierce
        # pour récupérer les informations de géolocalisation
    

        # Récupérer l'appareil et le navigateur utilisé par le client
    user_agent = request.user_agent
    device = user_agent.platform
    browser = user_agent.browser

        # Afficher les informations récupérées dans le terminal
    print('Adresse IP:', ip)
    print('Appareil:', device)
    print('Navigateur:', browser) 
    return render_template('index.html', reponse=reponse)


    

app.run(host='0.0.0.0', port=5000)


