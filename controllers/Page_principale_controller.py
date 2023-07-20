import pandas as pd



class Page_principale_controller:
    def __init__(self, df,gamme,specialites,region,ville):
        self.df = df
        self.gamme=gamme
        self.specialites=specialites
        self.region=region
        self.ville=ville


  
    def get_principale_data(self):

        result_dict = self.getStat(self.df)
        result_dict['region'] = self.getRegionDic(self.df,self.region,self.ville)
        result_dict['gammes'] = self.getGammeDic(self.df,self.gamme,self.specialites)
        finaleDic={'statistiques':result_dict}

    
        return finaleDic


    #function pour return region json
    def getRegionDic(self,df,regions_uniques,villes_uniques):

        # grouper les données par région et ville et compter le nombre de visites
        visites_par_region_ville = df.groupby(['region', 'ville'])['id_visite'].count().reset_index().rename(columns={'id_visite': 'nb_visites'})

        # grouper les données par région et compter le nombre de visites
        visites_par_region = visites_par_region_ville.groupby(['region'])['nb_visites'].sum().reset_index().rename(columns={'nb_visites': 'total_visites'})

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

            nb_visites = row['nb_visites']
            total_visites = row['total_visites']

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
                    "nb_visites_total": total_visites,
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
                    "nb_visites": nb_visites
                })

        # afficher le résultat au format JSON
        return resultats
    #function pour return gammes json
    def getGammeDic(self,df,gammes_uniques,specialites_uniques) : 

        # Grouper les données par gamme, code_gamme, spécialité et code_spécialité et compter le nombre de visites
        visites_par_gamme_specialite = df.groupby(['gamme', 'specialite'])['id_visite'].count().reset_index().rename(columns={'id_visite': 'nb_visites'})

        # Grouper les données par gamme et compter le nombre de visites
        visites_par_gamme = visites_par_gamme_specialite.groupby(['gamme'])['nb_visites'].sum().reset_index().rename(columns={'nb_visites': 'total_visites'})
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

            nb_visites = row['nb_visites']
            total_visites = row['total_visites']

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
                    'nbr_total_visites': total_visites,
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
                    'nb_visites_total': nb_visites
                })

        # afficher le résultat au format JSON
        return resultats
    # function pour return les stat 
    def getStat(self,df):
        listCol = ['code_type_partenaire', 'type_etablissement', 'type_visite', 'flag_accompagnee']
        FiltreVar = 'code_type_visite'
        result_dict = {}
        dicte={"HOPL":'non_planifiees',"PLAN":'planifiees',"MEDE":'medicales',
            "PHAR":"pharmaceutiques","ETPR":"privees","ETPU":"publiques",
            "S":"simple", "G":"groupe","N":"indiviuel","O":"en_double"}
        visites=df.groupby([FiltreVar])['id_visite'].count()
        for index, value in visites.items():
                    key = ( "nbr_total_visites_"+ dicte[index])
                    result_dict[key] = value
        for col in listCol:
            result = df.groupby([FiltreVar, col])['id_visite'].count()
            for index, value in result.items():
                if(index[1]!=''):
                    key = ( "nbr_visites_"+ dicte[index[1]]+"_"+dicte[index[0]])
                    result_dict[key] = value
        return result_dict

