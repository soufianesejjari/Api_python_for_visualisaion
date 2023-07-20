import pandas as pd
#import sqlalchemy as db
import config.config as config
def getEvaluation():
    engine = config.engine
    conn = engine.connect()
    # Récupérer les données des différentes tables dans des DataFrames
    det = pd.read_sql_query("SELECT id, id_evaluation, code_categorie, code_sous_categorie, point_obtenu as detailPoint, point_sur FROM tab_evaluation_detailed", conn)
    ev = pd.read_sql_query("SELECT id, id_createur, id_utilisateur_evalue, points_obtenu, points_total, date_integration FROM tab_evaluation", conn)
    tc = pd.read_sql_query("SELECT code_codification, libelle_codification FROM tab_par_codification", conn)
    u = pd.read_sql_query("SELECT id_utilisateur, concat(nom_utilisateur,' ', prenom_utilisateur)as FullName,role FROM tab_utilisateur", conn)
    tv = pd.read_sql_query("SELECT id_utilisateur, COUNT(id_visite) AS nombre_visites FROM tab_visite GROUP BY id_utilisateur", conn)

    # Fusionner les DataFrames
    merged = pd.merge(det, ev, left_on='id_evaluation', right_on='id')
    merged = pd.merge(merged, tc, left_on='code_categorie', right_on='code_codification', suffixes=('', '_categorie'))
    merged = pd.merge(merged, tc, left_on='code_sous_categorie', right_on='code_codification', suffixes=('', '_sous_categorie'))
    merged = pd.merge(merged, u, left_on='id_utilisateur_evalue', right_on='id_utilisateur', suffixes=('', '_utilisateur'))
    merged = pd.merge(merged, u, left_on='id_createur', right_on='id_utilisateur', suffixes=('', '_createur'))
    merged = pd.merge(merged, tv, left_on='id_utilisateur_evalue', right_on='id_utilisateur', how='left')

    # Sélectionner les colonnes souhaitées et renommer les colonnes
    resultats = merged[['id_x', 'id_createur', 'FullName_createur', 'role_createur', 'id_utilisateur_evalue', 'FullName', 'points_obtenu', 'points_total', 'code_categorie', 'code_sous_categorie', 'libelle_codification', 'libelle_codification_sous_categorie', 'detailPoint', 'date_integration', 'nombre_visites']]
    resultats.columns = ['id', 'id_createur', 'FullName_createur', 'role_createur', 'id_utilisateur', 'FullName_utilisateur', 'points_obtenus', 'points_total', 'code_categorie', 'code_sous_categorie', 'categorie', 'sous_categorie', 'point_Detail',  'date_integration', 'nombre_visites']
    #resultats = resultats.groupby(['id', 'id_createur', 'nom_createur', 'prenom_createur', 'role_createur', 'id_utilisateur', 'nom_utilisateur', 'prenom_utilisateur', 'points_obtenus', 'points_total', 'code_categorie', 'code_sous_categorie', 'categorie', 'sous_categorie', 'point_obtenu', 'point_sur', 'date_integration']).agg({'nombre_visites': 'sum'}).reset_index()

    # Afficher les résultats


        # Afficher le temps de réponse
    return resultats

