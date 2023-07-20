import threading

import sched, time
import models.Principale_model as model
import models.Evaluation_model as Evaluationmodel
import models.Investis_model as Investismodel


import datetime
import config.config as config





# Verrou pour synchroniser l'accès à la variable data
data_lock = threading.Lock()
data = None

# Planifier la fonction de mise à jour des données pour s'exécuter toutes les 5 minutes
scheduler = sched.scheduler(time.time, time.sleep)

def schedule_update_data():
    global data
    global dataEvaluation
    global dataEnvestis


    global regions_uniques
    global villes_uniques
    global gammes_uniques
    global specialites_uniques
    dataEvaluation=Evaluationmodel.getEvaluation()
    dataEnvestis=Investismodel.getInvist()
    
    global users
    new_data = model.getData()
    users=model.dfUser

    regions_uniques = model.dfRegion
# supprimer les doublons pour obtenir une liste unique de régions avec les codes de région partenaires
    villes_uniques =model.dfVille

# supprimer les doublons pour obtenir une liste unique de régions avec les codes de région partenaires
    gammes_uniques = model.dfGamme
# supprimer les doublons pour obtenir une liste unique de régions avec les codes de région partenaires
    specialites_uniques = model.dfSpecialite


    # Acquisition du verrou pour accéder à la variable data
    data_lock.acquire()

    try:
        data = new_data

    finally:
        # Libération du verrou une fois l'accès à la variable data terminé
        data_lock.release()

    print(f"Data updated at {datetime.datetime.now()}")


    # Planifier la prochaine mise à jour des données
    threading.Timer(config.timeMis, schedule_update_data).start()

# Planifier la fonction pour la première fois
schedule_update_data()