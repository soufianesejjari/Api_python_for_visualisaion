import pandas as pd
import json

class Page_Eealuation_controller:
    def __init__(self, df):
        self.df = df



    def get_evaluation_data(self):
      

        result_dict = self.getStatEvakuation(self.df)
        result_dict['categories'] = self.getCategoriesDic(self.df)
        return result_dict

    def getCategoriesDic(self,df):
    # Supprimer les doublons pour obtenir une liste unique de catégories avec les codes de catégorie partenaires
        categories_uniques = df[['categorie', 'code_categorie']].drop_duplicates()

        # Supprimer les doublons pour obtenir une liste unique de sous-catégories avec les codes de sous-catégorie partenaires
        sous_categories_uniques = df[['categorie','sous_categorie', 'code_sous_categorie']].drop_duplicates()

        # Grouper les données par catégorie, sous-catégorie et calculer la moyenne de points_obtenus

        moyenne_points_categorie = df.groupby(['categorie'])['points_obtenus'].mean().to_dict()

        # Grouper les données par sous-catégorie et calculer la moyenne de point_Detail
        moyenne_points_sous_categorie = df.groupby(['sous_categorie'])['point_Detail'].mean().to_dict()

        # Joindre les deux DataFrames pour avoir la moyenne de points par catégorie et sous-catégorie
        resultat = pd.merge(categories_uniques, sous_categories_uniques, left_on='categorie', right_on='categorie', how='left')
        resultat = pd.merge(categories_uniques, sous_categories_uniques, left_on='categorie', right_on='categorie', how='left')

        # Créer une liste pour stocker les résultats finaux
        resultats = []

        # Parcourir les lignes du DataFrame et construire la liste de résultats
        for _, row in resultat.iterrows():
            categorie = row['categorie']
            code_categorie = row['code_categorie']
            sous_categorie = row['sous_categorie']
            code_sous_categorie = row['code_sous_categorie']

            # Chercher si la catégorie est déjà dans la liste des résultats
            index = None
            for i, result in enumerate(resultats):
                if result['categorie'] == categorie:
                    index = i
                    break

            # Si la catégorie n'est pas encore présente dans la liste des résultats, l'ajouter
            if index is None:
                resultats.append({
                    'code_categorie': code_categorie,
                    'categorie': categorie,
                    'moyenne_points_categorie': moyenne_points_categorie[categorie],
                    'sous_categories': []
                })
                index = len(resultats) - 1

            # Ajouter la sous-catégorie actuelle à la liste des sous-catégories de la catégorie
            if sous_categorie != "":
                resultats[index]["sous_categories"].append({
                    "code_sous_categorie": code_sous_categorie,
                    'sous_categorie': sous_categorie,
                    'moyenne_points_sous_categorie': moyenne_points_sous_categorie[sous_categorie]
                })

        # Afficher le résultat au format JSON
        return resultats
    def getStatEvakuation(self, df):
    # Nombre de visites par rapport au moyen d'évaluation
        visites_moyen_evaluation = df.groupby("points_obtenus")["nombre_visites"].sum().reset_index().to_dict(orient='records')

        # Nombre d'évaluation par Mois
        evaluations_mois = df.groupby(df["date_integration"].dt.strftime("%Y-%m")).size().reset_index()
        evaluations_mois.columns = ['date_integration', 'Nombre_evaluation']
        evaluations_mois = evaluations_mois.to_dict(orient='records')

        # Nombre d'évaluations par rôle
        pourcentage_evaluations_role = df.groupby("role_createur").size().reset_index()
        pourcentage_evaluations_role.columns = ['role_createur', 'Nombre_evaluation']
        pourcentage_evaluations_role = pourcentage_evaluations_role.to_dict(orient='records')

        # Moyenne de points_obtenus par les utilisateurs
        moyenne_points_utilisateurs = df.groupby("FullName_utilisateur")["points_obtenus"].mean().reset_index()
        moyenne_points_utilisateurs.columns = ['FullName_utilisateur', 'points_obtenus']
        moyenne_points_utilisateurs = moyenne_points_utilisateurs.to_dict(orient='records')

        # Créer un dictionnaire avec les résultats
        resultats = {
            'Nombre_visites_par_moyen_evaluation': visites_moyen_evaluation,
            'Nombre_evaluation_par_Mois': evaluations_mois,
            'pourcentage_evaluations_role': pourcentage_evaluations_role,
            'moyenne_points_utilisateurs': moyenne_points_utilisateurs
        }
        return resultats
