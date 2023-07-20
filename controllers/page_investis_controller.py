import pandas as pd
import json

class Page_Invest_controller:
    def __init__(self, df,gamme,specialites,region,ville):
        self.df = df
        self.gamme=gamme
        self.specialites=specialites
        self.region=region
        self.ville=ville
    def get_Invest_data(self):
    
        return self.getInvis(self.df,self.region,self.gamme,self.specialites)

    def getInvis(self, df, region, gamme, specialites):
        # Groupby par Nombre de nombre de visites et calculer la somme des budgets
        budget_par_visites = df.groupby('nombre_visite')['budget'].sum().reset_index().rename(columns={'nombre_visite': 'Nombre de nombre de visites'})

        # Groupby par code_gamme et calculer la somme des budgets
        budget_par_gamme = df.groupby('code_gamme')['budget'].sum().reset_index()
        budget_par_gamme = budget_par_gamme.merge(gamme, left_on='code_gamme', right_on='code_gamme_partenaire', how='left')

        # Groupby par statut et calculer la somme des budgets
        budget_par_statut = df.groupby('code_statut_bc')['budget'].sum().reset_index()

        # Groupby par potentiel et calculer la somme des budgets
        budget_par_potentiel = df.groupby('code_potentiel')['budget'].sum().reset_index()

        # Groupby par specialite et calculer la somme des budgets
        budget_par_specialite = df.groupby('code_specialite')['budget'].sum().reset_index()
        budget_par_specialite = budget_par_specialite.merge(specialites, left_on='code_specialite', right_on='code_specialite_partenaire', how='left')

        # Groupby par region et calculer la somme des budgets
        budget_par_region = df.groupby('code_region_partenaire')['budget'].sum().reset_index()
        budget_par_region = budget_par_region.merge(region, left_on='code_region_partenaire', right_on='code_region_partenaire', how='left')

        # Groupby par type d'investissement et calculer la somme des budgets
        budget_par_type_investissement = df.groupby('code_type_investissement')['budget'].sum().reset_index()

        # Groupby par categorie d'investissement et calculer la somme des budgets
        budget_par_categorie_investissement = df.groupby('code_categorie_investissement')['budget'].sum().reset_index()

        # Créer un dictionnaire avec les résultats
        resultats = {
            'budget_par_visites': budget_par_visites.to_dict(orient='records'),
            'budget_par_gamme': budget_par_gamme.to_dict(orient='records'),
            'budget_par_statut': budget_par_statut.to_dict(orient='records'),
            'budget_par_potentiel': budget_par_potentiel.to_dict(orient='records'),
            'budget_par_specialite': budget_par_specialite.to_dict(orient='records'),
            'budget_par_region': budget_par_region.to_dict(orient='records'),
            'budget_par_type_investissement': budget_par_type_investissement.to_dict(orient='records'),
            'budget_par_categorie_investissement': budget_par_categorie_investissement.to_dict(orient='records')
        }

        return resultats

