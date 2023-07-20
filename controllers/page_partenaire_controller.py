import pandas as pd
import json

class Page_partenaire_controller:
    def __init__(self, df,gamme,specialites,region,ville):
        self.df = df
        self.gamme=gamme
        self.specialites=specialites
        self.region=region
        self.ville=ville

    def get_partenaire_data(self):


        df=self.df.drop_duplicates(subset='id_partenaire', keep='first')

        # Groupby par ville et compter le nombre de comptes
        comptes_ville = df.groupby("ville")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})

        # Groupby par potentiel et compter le nombre de comptes
        comptes_potentiel = df.groupby("code_potentiel")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})
        # Groupby par spécialité et compter le nombre de comptes
        #comptes_specialite = df.groupby("specialite")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})

        # Calculer le nombre de visites moyen par compte
        visites_moyen = self.df.groupby("id_partenaire")["id_visite"].nunique().mean()

        # Groupby par région et compter le nombre de comptes
        #comptes_region = df.groupby("region")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})

        # Groupby par établissement et compter le nombre de comptes
        comptes_etablissement = df.groupby("etablissement")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})

        # Créer un dictionnaire avec les résultats
        resultats = {

            
            "Nombre_de_comptes_par_potentiel":comptes_potentiel.to_dict(orient='records'),



            "Nombre_de_visites_moyen": visites_moyen,
        

            "Nombre_de_comptes_par_etablissement": comptes_etablissement.to_dict(orient='records'),
            "region_partenaire": self.getRegionDicP(df,self.region,self.ville),
            
            "gamme_partenaire":self.getGammeDicP(df,self.gamme,self.specialites)

        }
        return resultats


        
    def getRegionDicP(self,df,regions_uniques,villes_uniques):

        # grouper les données par région et ville et compter le nombre de visites
        visites_par_region_ville = df.groupby(['region', 'ville'])['id_partenaire'].nunique().reset_index().rename(columns={'id_partenaire': 'nb_partenaire'})

        # grouper les données par région et compter le nombre de visites
        visites_par_region = visites_par_region_ville.groupby(['region'])['nb_partenaire'].sum().reset_index().rename(columns={'nb_partenaire': 'total_partenaire'})

        # joindre les deux DataFrames pour avoir le nombre de visites par région et par ville
        resultat = pd.merge(visites_par_region_ville, visites_par_region, on='region', how='left')
        resultat = pd.merge(resultat, villes_uniques, on='ville', how='left')
        resultat = pd.merge(resultat, regions_uniques, on='region', how='left')

        # créer une liste pour stocker les résultats finaux
        resultats = []

        # parcourir les lignes du DataFrame et construire la liste de résultats
        for _, row in resultat.iterrows():
            region = row['region']
            code_region_partenaire = row['code_region_partenaire']

            ville = row['ville']
            code_ville_partenaire = row['code_ville_partenaire']

            nb_visites = row['nb_partenaire']
            total_visites = row['total_partenaire']

            # chercher si la région est déjà dans la liste des résultats
            index = None
            for i, result in enumerate(resultats):
                if result['region'] == region:
                    index = i
                    break

            # si la région n'est pas encore présente dans la liste des résultats, l'ajouter
            if index is None:
                resultats.append({
                    'code_region_partenaire':code_region_partenaire,

                    'region':region ,
                    "total_partenaire": total_visites,
                    "ville": []
                })
                index = len(resultats) - 1

            # ajouter la ville actuelle à la liste des villes de la région
            if nb_visites > 0:
                resultats[index]["ville"].append({
                    'code_ville_partenaire':code_ville_partenaire,
                    'code_region_partenaire':code_region_partenaire,
                    "ville": ville,
                    "region": region,
                    "nb_partenaire": nb_visites
                })

        # afficher le résultat au format JSON
        return resultats
#function pour return gammes json
    def getGammeDicP(self,df,gammes_uniques,specialites_uniques) : 

        # Grouper les données par gamme, code_gamme, spécialité et code_spécialité et compter le nombre de visites
        visites_par_gamme_specialite = df.groupby(['gamme', 'specialite'])['id_partenaire'].nunique().reset_index().rename(columns={'id_partenaire': 'nb_partenaire'})

        # Grouper les données par gamme et compter le nombre de visites
        visites_par_gamme = visites_par_gamme_specialite.groupby(['gamme'])['nb_partenaire'].sum().reset_index().rename(columns={'nb_partenaire': 'total_partenaire'})
        resultat = pd.merge(visites_par_gamme_specialite, visites_par_gamme, on=['gamme'], how='left')

        resultat = pd.merge(resultat, gammes_uniques, on='gamme', how='left')
        resultat = pd.merge(resultat, specialites_uniques, on='specialite', how='left')



        # Joindre les deux DataFrames pour avoir le nombre de visites par gamme, code_gamme, spécialité et code_spécialité
        # créer une liste pour stocker les résultats finaux
        resultats = []

        # parcourir les lignes du DataFrame et construire la liste de résultats
        for _, row in resultat.iterrows():
            gamme = row['gamme']
            code_gamme = row['code_gamme_partenaire']
            specialite = row['specialite']
            code_specialite = row['code_specialite_partenaire']

            nb_visites = row['nb_partenaire']
            total_visites = row['total_partenaire']

            # chercher si la région est déjà dans la liste des résultats
            index = None
            for i, result in enumerate(resultats):
                if result['gamme'] == gamme:
                    index = i
                    break

            # si la région n'est pas encore présente dans la liste des résultats, l'ajouter
            if index is None:
                resultats.append({
                    'code_gamme': code_gamme,
                    'gamme': gamme,
                    'total_partenaire': total_visites,
                    'specialites': []
                })
                index = len(resultats) - 1

            # ajouter la ville actuelle à la liste des specialites de la gammme
            if nb_visites > 0:
                resultats[index]["specialites"].append({
                    "code_specialite": code_specialite,

                'specialite': specialite,
                    'gamme': gamme,
                    'code_gamme': code_gamme,
                    'nb_partenaire': nb_visites
                })

        # afficher le résultat au format JSON
        return resultats
