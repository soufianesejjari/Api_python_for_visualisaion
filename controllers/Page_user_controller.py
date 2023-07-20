import pandas as pd

class PageUser:
    def __init__(self, df,gamme,specialites,region,ville):
        self.df = df
        self.gamme=gamme
        self.specialites=specialites
        self.region=region
        self.ville=ville


    def get_user_data(self):


        charts_data = {}

        # Nombre de nouvelle utilisateur par Mois
        self.df['date_visite'] = pd.to_datetime(self.df['date_visite'])
        self.df['mois'] = self.df['date_visite'].dt.month
        new_users_by_month = self.df.groupby('mois')['id_utilisateur'].nunique().reset_index()
        charts_data['nombre_nouvelle_utilisateur_par_mois'] =[
            {
                'mois': statut,
                'nombre_utilisateur': nombre_utilisateur
            }
            for statut, nombre_utilisateur in zip(new_users_by_month['mois'].tolist(), new_users_by_month['id_utilisateur'].tolist())
        ]

        # Nombre d'utilisateur par Gammes
        users_by_gamme = self.df.groupby('code_gamme_partenaire')['id_utilisateur'].nunique().reset_index().rename(columns={'id_utilisateur': 'nombre_utilisateur'})
        users_by_gamme = pd.merge(users_by_gamme, self.gamme, on='code_gamme_partenaire', how='left')

        charts_data['nombre_utilisateur_par_gammes'] = users_by_gamme.to_dict(orient='records')

        # Pourcentage de visités par responsable
        visited_percentage_by_responsable = self.df.groupby('COALESCE(tv.id_responsable, 0)')['id_visite'].count()
        visited_percentage_by_responsable = visited_percentage_by_responsable.reset_index()
        
        charts_data['pourcentage_visites_par_responsable'] =[
            {
                'id_responsable': responsable,
                'nombre_visites': visites
            }
            for responsable, visites in zip(visited_percentage_by_responsable['COALESCE(tv.id_responsable, 0)'].tolist(), visited_percentage_by_responsable['id_visite'].tolist())
        ]

        # Nombre d'utilisateur par Régions
        users_by_region = self.df.groupby('region')['id_utilisateur'].nunique().reset_index().rename(columns={'id_utilisateur': 'nombre_utilisateur'})
        users_by_region = pd.merge(users_by_region, self.region, on='region', how='left')

        charts_data['nombre_utilisateur_par_regions'] =users_by_region.to_dict(orient='records')

        # Nombre d'utilisateur par Status
        users_by_status = self.df.groupby('code_statut_partenaire')['id_utilisateur'].nunique().reset_index()
        charts_data['nombre_utilisateur_par_status'] = [
            {
                'code_statut_partenaire': statut,
                'nombre_utilisateur': nombre_utilisateur
            }
            for statut, nombre_utilisateur in zip(users_by_status['code_statut_partenaire'].tolist(), users_by_status['id_utilisateur'].tolist())
        ]

        # Nombre d'utilisateur par Rôle
        users_by_role = self.df.groupby('role')['id_utilisateur'].nunique().reset_index()
        charts_data['nombre_utilisateur_par_role'] = [
            {
                'role': role,
                'nombre_utilisateur': nombre_utilisateur
            }
            for role, nombre_utilisateur in zip(users_by_role['role'].tolist(), users_by_role['id_utilisateur'].tolist())
        ]

        return charts_data
