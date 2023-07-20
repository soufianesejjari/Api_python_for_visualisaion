import pandas as pd
#import sqlalchemy as db
import config.config as config
def getInvist():
    engine = config.engine
    connection = engine.connect()
    # Chargement des données depuis la base de données
    tab_partenaire_bc = pd.read_sql_query("SELECT id_business_case, id_partenaire, id_responsable, code_statut_bc, code_type_investissement, code_categorie_investissement, budget, date_realisation FROM tab_partenaire_bc", connection)
    tab_par_codification = pd.read_sql_query("SELECT code_codification, libelle_codification FROM tab_par_codification", connection)
    tab_utilisateur = pd.read_sql_query("SELECT id_utilisateur, CONCAT(nom_utilisateur, ' ', prenom_utilisateur) as fullName_responsable FROM tab_utilisateur", connection)
    tab_partenaire = pd.read_sql_query("SELECT id_partenaire,CONCAT(nom_partenaire, ' ', prenom_partenaire) as fullName_partenaire, code_gamme, code_potentiel, code_specialite, code_type_partenaire, code_region_partenaire, code_ville_partenaire FROM tab_partenaire", connection)
    tab_partenaire_visite = pd.read_sql_query("SELECT id_partenaire, COUNT(id_visite) as nombre_visite FROM tab_partenaire_visite GROUP BY id_partenaire", connection)

    # Jointure des tables
    merged_data = tab_partenaire_bc.merge(tab_par_codification, left_on='code_type_investissement', right_on='code_codification', how='left')
    merged_data = merged_data.merge(tab_par_codification, left_on='code_categorie_investissement', right_on='code_codification', suffixes=('_type', '_categorie'), how='left')
    merged_data = merged_data.merge(tab_utilisateur, left_on='id_responsable', right_on='id_utilisateur', how='left')
    merged_data = merged_data.merge(tab_partenaire, left_on='id_partenaire', right_on='id_partenaire', how='left')
    merged_data = merged_data.merge(tab_partenaire_visite, left_on='id_partenaire', right_on='id_partenaire', how='left')

    # Sélection des colonnes nécessaires
    result_data = merged_data[['id_business_case', 'id_partenaire', 'fullName_partenaire', 'id_responsable', 'fullName_responsable', 'code_statut_bc', 'code_type_investissement', 'libelle_codification_type', 'code_categorie_investissement', 'libelle_codification_categorie', 'code_gamme', 'code_potentiel', 'code_specialite', 'code_type_partenaire', 'code_region_partenaire', 'code_ville_partenaire', 'budget', 'nombre_visite', 'date_realisation']]

    # Groupement par id_partenaire
    result_data = result_data.groupby('id_partenaire').agg({
        'id_business_case': 'first',
        'fullName_partenaire': 'first',
        'id_responsable': 'first',
        'fullName_responsable': 'first',
        'code_statut_bc': 'first',
        'code_type_investissement': 'first',
        'libelle_codification_type': 'first',
        'code_categorie_investissement': 'first',
        'libelle_codification_categorie': 'first',
        'code_gamme': 'first',
        'code_potentiel': 'first',
        'code_specialite': 'first',
        'code_type_partenaire': 'first',
        'code_region_partenaire': 'first',
        'code_ville_partenaire': 'first',
        'budget': 'first',
        'nombre_visite': 'sum',
        'date_realisation': 'first'
    }).reset_index()

    # Affichage des résultats
    return result_data

