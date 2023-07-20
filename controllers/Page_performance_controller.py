import pandas as pd

class Page2Controller:
    def __init__(self, df):
        self.df = df
    
    def get_page2_data(self):


        # Grouper les données
        groupe_type_compte = self.df.groupby('code_type_partenaire')['id_visite'].nunique().reset_index()
        groupe_status = self.df.groupby('code_statut_partenaire')['id_visite'].nunique().reset_index()
        groupe_region = self.df.groupby('region')['id_visite'].nunique().reset_index()
        groupe_utilisateur = self.df.groupby('fullName_utilisateur')['id_visite'].nunique().nlargest(5).reset_index()
        groupe_delegues = self.df.groupby('COALESCE(tv.id_responsable, 0)')['id_visite'].nunique().nsmallest(5).reset_index()
        groupe_jour = self.df.groupby(pd.Grouper(key='date_visite', freq='D'))['id_visite'].nunique().reset_index()
        group_potonciel = self.df.groupby('code_potentiel').size().reset_index()

        # Créer un dictionnaire avec les résultats
        resultats = {
            'nombre_compte_visite_par_type_compte': [
                {
                    'code_type_partenaire': type_compte,
                    'nombre_visites': nombre_visites
                }
                for type_compte, nombre_visites in zip(groupe_type_compte['code_type_partenaire'].tolist(), groupe_type_compte['id_visite'].tolist())
            ],
            'nombre_compte_visite_par_status': [
                {
                    'code_statut_partenaire': statut,
                    'nombre_visites': nombre_visites
                }
                for statut, nombre_visites in zip(groupe_status['code_statut_partenaire'].tolist(), groupe_status['id_visite'].tolist())
            ],
            'nombre_visites_par_potenciel': [
                {
                    'code_potentiel': potenciel,
                    'nombre_visites': nombre_visites
                }
                for potenciel, nombre_visites in zip(group_potonciel['code_potentiel'].tolist(), group_potonciel[0].tolist())
            ],
            'nombre_visites_par_region': [
                {
                    'region': region,
                    'nombre_visites': nombre_visites
                }
                for region, nombre_visites in zip(groupe_region['region'].tolist(), groupe_region['id_visite'].tolist())
            ],
            'utilisateurs_plus_grand_nombre_visites': [
                {
                    'delegue': utilisateur,
                    'nombre_visites': nombre_visites
                }
                for utilisateur, nombre_visites in zip(groupe_utilisateur['fullName_utilisateur'].tolist(), groupe_utilisateur['id_visite'].tolist())
            ],
            'delegues_moins_nombre_visites': [
                {
                    'delegue': delegue,
                    'nombre_visites': nombre_visites
                }
                for delegue, nombre_visites in zip(groupe_delegues['COALESCE(tv.id_responsable, 0)'].tolist(), groupe_delegues['id_visite'].tolist())
            ],
            'nombre_compte_visite_par_jour': [
                {
                    'date_visite': date.strftime('%Y-%m-%d'),
                    'nombre_visites': nombre_visites
                }
                for date, nombre_visites in zip(groupe_jour['date_visite'].tolist(), groupe_jour['id_visite'].tolist())
            ]
        }

        return resultats
