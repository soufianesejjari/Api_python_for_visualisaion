import pandas as pd
from models.Object_model import Object_Model as ObjecModel
from models.Object_model import Object_Invest as Object_Invest
from models.Object_model import Object_Evaluation

class Filtrage_controller:
    def __init__(self, df, users):
        self.df = df
        self.users = users

    def get_users_of_responsable(self, df, responsable_id):
        # Obtient tous les utilisateurs d'un responsable (récursivement)
        users_of_responsable = [responsable_id]
        responsables_to_check = [responsable_id]

        while responsables_to_check:
            current_responsable = responsables_to_check.pop(0)
            users = df[df['id_responsable'] == current_responsable]['id_utilisateur'].tolist()

            for user in users:
                role = df[df['id_utilisateur'] == user]['role'].values[0]
                if 'del' not in role:
                    users_of_responsable.append(user)
                    responsables_to_check.append(user)

        return users_of_responsable

    def get_filtered_data(self,request : ObjecModel):
        """
        Récupère les données filtrées en fonction des paramètres d'entrée.

        Args:
            id_responsable (int): ID du responsable.
            id_utilisateur (int): ID de l'utilisateur.
            annee (int): Année de la visite.
            mois (int): Mois de la visite.
            gamme (str): Gamme des partenaires.
            region (str): Région des partenaires.
            start_date (datetime.date): Date de début de la période spécifiée.
            end_date (datetime.date): Date de fin de la période spécifiée.

        Returns:
            pandas.DataFrame: Données filtrées.

        """
        id_responsable = request.id_responsable
        id_utilisateur = request.id_utilisateur
        annee = request.annee
        mois = request.mois
        gamme = request.gamme
        region = request.region
        start_date = request.start_date
        end_date = request.end_date


        # Filtrer les données en fonction des paramètres d'entrée
        if id_responsable is not None:
            self.df = self.df[self.df['id_utilisateur'].isin(self.get_users_of_responsable(self.users, id_responsable))]

        if id_utilisateur is not None:
            self.df = self.df[self.df['id_utilisateur'] == int(id_utilisateur)]

        if annee is not None:
            self.df = self.df[self.df['date_visite'].dt.year == int(annee)]

        if mois is not None:
            self.df = self.df[self.df['date_visite'].dt.month == int(mois)]

        if gamme is not None:
            self.df = self.df[self.df['code_gamme_partenaire'] == gamme]

        if region is not None:
            self.df = self.df[self.df['code_region_partenaire'] == region]

        if start_date is not None and end_date is not None:
            self.df = self.df[(self.df['date_visite'] >= start_date) & (self.df['date_visite'] <= end_date)]

        return self.df
    def get_filtered_Invest(self,request : Object_Invest):
        code_type_investissement=request.code_type_investissement

        id_responsable = request.id_responsable
        id_partenaire = request.id_partenaire

 
        region = request.region
        start_date = request.start_date
        end_date = request.end_date


        # Filtrer les données en fonction des paramètres d'entrée
        if id_responsable is not None:
            self.df = self.df[self.df['id_responsable']== int(id_responsable)]

        if id_partenaire is not None:
            self.df = self.df[self.df['id_partenaire'] == int(id_partenaire)]


        if code_type_investissement is not None:
            self.df = self.df[self.df['code_type_investissement'] == code_type_investissement]

        if region is not None:
            self.df = self.df[self.df['code_region_partenaire'] == region]

        if start_date is not None and end_date is not None:
            self.df = self.df[(self.df['date_integration'] >= start_date) & (self.df['date_integration'] <= end_date)]

        return self.df
    def get_filtered_Evaluation(self,request : Object_Evaluation):
        id_utilisateur=request.id_utilisateur

        code_categorie = request.code_categorie
   
        start_date = request.start_date
        end_date = request.end_date


        # Filtrer les données en fonction des paramètres d'entrée
        if id_utilisateur is not None:
            self.df = self.df[self.df['id_utilisateur']== int(id_utilisateur)]

        if code_categorie is not None:
            self.df = self.df[self.df['code_categorie'] == str(code_categorie)]


   

        if start_date is not None and end_date is not None:
            self.df = self.df[(self.df['date_integration'] >= start_date) & (self.df['date_integration'] <= end_date)]

        return self.df
