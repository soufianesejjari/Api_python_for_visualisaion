import pandas as pd
#import sqlalchemy as db
import config.config as config
def getDBv2():
    engine = config.engine
    con = engine.connect()


    # deuxième requête
    query2 = "SELECT tv.id_visite, tv.id_utilisateur, COALESCE(tv.id_responsable, 0), tv.code_type_visite, tv.code_statut_visite,flag_accompagnee, DATE(tv.date_visite) as date_visite, tv.heure_fin_visite, tv.type_visite FROM tab_visite tv"
    df2 = pd.read_sql(query2, con)

    # troisième requête
    query3 = "SELECT id_visite, id_partenaire, code_region_partenaire, code_ville_partenaire, code_type_partenaire, code_gamme_partenaire, code_specialite_partenaire FROM tab_partenaire_visite"
    df3 = pd.read_sql(query3, con)

    # fusion des tables
    merged_df = pd.merge(df2, df3, on='id_visite', how='outer', suffixes=('_partenaire', '_visite'))
    #merged_df = pd.merge(merged_df, df3, on='id_visite', how='outer', suffixes=('', '_partenaire'))
    
    query4 ="SELECT id_utilisateur, CONCAT(nom_utilisateur, ' ', prenom_utilisateur) as fullName_utilisateur FROM tab_utilisateur"
    dfUser = pd.read_sql(query4, con)
    merged_df = pd.merge(merged_df, dfUser, on='id_utilisateur', how='left')

    query5 ="SELECT `id_partenaire`,concat(`nom_partenaire`,' ',`prenom_partenaire`) as FullNamePartenaire,`code_potentiel`,code_type_etablissement,code_statut_partenaire FROM `tab_partenaire`"
    dfPar = pd.read_sql(query5, con)
    merged_df = pd.merge(merged_df, dfPar, on='id_partenaire', how='left')

    query6 ="SELECT `code_codification` as code_ville_partenaire,`libelle_codification` as ville FROM `tab_par_codification`"
    dfVille = pd.read_sql(query6, con)
    merged_df = pd.merge(merged_df, dfVille, on='code_ville_partenaire', how='left')

    query7 ="SELECT `code_codification` as code_region_partenaire,`libelle_codification` as region FROM `tab_par_codification`"
    dfRegion = pd.read_sql(query7, con)
    merged_df = pd.merge(merged_df, dfRegion, on='code_region_partenaire', how='left')
    query9 ="SELECT `code_codification` as code_specialite_partenaire,`libelle_codification` as specialite FROM `tab_par_codification`"
    dfSpecialite = pd.read_sql(query9, con)
    merged_df = pd.merge(merged_df, dfSpecialite, on='code_specialite_partenaire', how='left')
    
    query10 ="SELECT `code_codification` as code_type_etablissement,type_codification as type_etablissement,`libelle_codification` as etablissement FROM `tab_par_codification`"
    dfEtab = pd.read_sql(query10, con)
    merged_df = pd.merge(merged_df, dfEtab, on='code_type_etablissement', how='left')

    query11 ="SELECT `code_codification` as code_gamme_partenaire,`libelle_codification` as gamme FROM `tab_par_codification`"
    dfRegion = pd.read_sql(query11, con)
    merged_df = pd.merge(merged_df, dfRegion, on='code_gamme_partenaire', how='left')                                   
    # Convertir les colonnes avec des valeurs nulles en types de données appropriés
    merged_df['id_visite'] = merged_df['id_visite'].astype('Int32')
    #merged_df['id_produit'] = merged_df['id_produit'].astype('Int32')
    #merged_df['nbr_echantillon'] = merged_df['nbr_echantillon'].astype('Int32')
    merged_df['id_utilisateur'] = merged_df['id_utilisateur'].astype('Int32')
    merged_df['COALESCE(tv.id_responsable, 0)'] = merged_df['COALESCE(tv.id_responsable, 0)'].astype('Int32')
    merged_df['id_partenaire'] = merged_df['id_partenaire'].astype('Int32')

    # Convertir les colonnes avec des types d'objet en types de catégorie appropriés
    #merged_df['code_gamme'] = merged_df['code_gamme'].astype('category')
    merged_df['code_type_visite'] = merged_df['code_type_visite'].astype('category')
    merged_df['code_statut_visite'] = merged_df['code_statut_visite'].astype('category')
    merged_df['type_visite'] = merged_df['type_visite'].astype('category')
    merged_df['code_region_partenaire'] = merged_df['code_region_partenaire'].astype('category')
    merged_df['code_ville_partenaire'] = merged_df['code_ville_partenaire'].astype('category')
    merged_df['code_type_partenaire'] = merged_df['code_type_partenaire'].astype('category')
    merged_df['code_gamme_partenaire'] = merged_df['code_gamme_partenaire'].astype('category')
    merged_df['code_specialite_partenaire'] = merged_df['code_specialite_partenaire'].astype('category')
    merged_df['code_potentiel'] = merged_df['code_potentiel'].astype('category')
    merged_df['code_statut_partenaire'] = merged_df['code_statut_partenaire'].astype('category')
    merged_df['ville'] = merged_df['ville'].astype('category')
    merged_df['region'] = merged_df['region'].astype('category')
    merged_df['specialite'] = merged_df['specialite'].astype('category')
    merged_df['gamme'] = merged_df['gamme'].astype('category')
    merged_df['etablissement'] = merged_df['etablissement'].astype('category')
    merged_df['flag_accompagnee'] = merged_df['flag_accompagnee'].astype('category')
    merged_df['type_etablissement'] = merged_df['type_etablissement'].astype('category')


    


    # Convertir les colonnes avec des types de temps en types de données appropriés
    merged_df['heure_fin_visite'] = pd.to_timedelta(merged_df['heure_fin_visite'])
    merged_df['date_visite'] =   pd.to_datetime(merged_df['date_visite'])
       # close connexion 
    con.close()
    # affichage du résultat
    return merged_df
def getData():
   engine = config.engine
   con = engine.connect()
   # deuxième requête
   query2 = "SELECT tv.id_visite, tv.id_utilisateur, COALESCE(tv.id_responsable, 0), tv.code_type_visite, tv.code_statut_visite,flag_accompagnee, DATE(tv.date_visite) as date_visite,  tv.type_visite FROM tab_visite tv"
   df2 = pd.read_sql(query2, con)

   # troisième requête
   query3 = "SELECT id_visite, id_partenaire, code_region_partenaire, code_ville_partenaire, code_type_partenaire, code_gamme_partenaire, code_specialite_partenaire FROM tab_partenaire_visite"
   df3 = pd.read_sql(query3, con)

   # fusion des tables
   merged_df = pd.merge(df2, df3, on='id_visite', how='outer', suffixes=('_partenaire', '_visite'))
   #merged_df = pd.merge(merged_df, df3, on='id_visite', how='outer', suffixes=('', '_partenaire'))

   
   query4 ="SELECT id_utilisateur,id_responsable, CONCAT(nom_utilisateur, ' ', prenom_utilisateur) as fullName_utilisateur,role FROM tab_utilisateur"
   global dfUser

   dfUser = pd.read_sql(query4, con)
   merged_df = pd.merge(merged_df, dfUser, on='id_utilisateur', how='left')

   query5 ="SELECT `id_partenaire`,concat(`nom_partenaire`,' ',`prenom_partenaire`) as FullNamePartenaire,`code_potentiel`,code_type_etablissement,code_statut_partenaire FROM `tab_partenaire`"
   dfPar = pd.read_sql(query5, con)
   merged_df = pd.merge(merged_df, dfPar, on='id_partenaire', how='left')

   query = "SELECT `code_codification`, `libelle_codification`, `type_codification` FROM `tab_par_codification`"
   dfCodification = pd.read_sql(query, con)

   global dfVille

   global dfRegion
   global dfSpecialite

   global dfEtab
   global dfGamme

   # Filtrer les données pour chaque besoin spécifique
   dfVille = dfCodification[dfCodification['type_codification'] == 'VILL'].rename(columns={'code_codification': 'code_ville_partenaire', 'libelle_codification': 'ville'})
   dfRegion = dfCodification[dfCodification['type_codification'] == 'REGI'].rename(columns={'code_codification': 'code_region_partenaire', 'libelle_codification': 'region'})
   dfSpecialite = dfCodification[dfCodification['type_codification'] == 'SPEC'].rename(columns={'code_codification': 'code_specialite_partenaire', 'libelle_codification': 'specialite'})
   dfEtab = dfCodification[dfCodification['type_codification'].isin(['ETPR', 'ETPU'])].rename(columns={'type_codification':'type_etablissement','code_codification': 'code_type_etablissement', 'libelle_codification': 'etablissement'})
   dfGamme = dfCodification[dfCodification['type_codification'] == 'GAMM'].rename(columns={'code_codification': 'code_gamme_partenaire', 'libelle_codification': 'gamme'})

   # Supprimer la colonne 'type_codification' des DataFrames
   dfVille.drop('type_codification', axis=1, inplace=True)
   dfRegion.drop('type_codification', axis=1, inplace=True)
   dfSpecialite.drop('type_codification', axis=1, inplace=True)
   dfGamme.drop('type_codification', axis=1, inplace=True)

   # Effectuer les jointures avec le DataFrame principal
   merged_df = pd.merge(merged_df, dfVille, on='code_ville_partenaire', how='left')
   merged_df = pd.merge(merged_df, dfRegion, on='code_region_partenaire', how='left')
   merged_df = pd.merge(merged_df, dfSpecialite, on='code_specialite_partenaire', how='left')
   merged_df = pd.merge(merged_df, dfEtab, on='code_type_etablissement', how='left')
   merged_df = pd.merge(merged_df, dfGamme, on='code_gamme_partenaire', how='left')
                                    
   # Convertir les colonnes avec des valeurs nulles en types de données appropriés
   merged_df['id_visite'] = merged_df['id_visite'].astype('Int32')
   #merged_df['id_produit'] = merged_df['id_produit'].astype('Int32')
   #merged_df['nbr_echantillon'] = merged_df['nbr_echantillon'].astype('Int32')
   merged_df['id_utilisateur'] = merged_df['id_utilisateur'].astype('Int32')
   merged_df['COALESCE(tv.id_responsable, 0)'] = merged_df['COALESCE(tv.id_responsable, 0)'].astype('Int32')
   merged_df['id_partenaire'] = merged_df['id_partenaire'].astype('Int32')

   # Convertir les colonnes avec des types d'objet en types de catégorie appropriés
   #merged_df['code_gamme'] = merged_df['code_gamme'].astype('category')
   merged_df['code_type_visite'] = merged_df['code_type_visite'].astype('category')
   merged_df['code_statut_visite'] = merged_df['code_statut_visite'].astype('category')
   merged_df['type_visite'] = merged_df['type_visite'].astype('category')
   merged_df['code_region_partenaire'] = merged_df['code_region_partenaire'].astype('category')
   merged_df['code_ville_partenaire'] = merged_df['code_ville_partenaire'].astype('category')
   merged_df['code_type_partenaire'] = merged_df['code_type_partenaire'].astype('category')
   merged_df['code_gamme_partenaire'] = merged_df['code_gamme_partenaire'].astype('category')
   merged_df['code_specialite_partenaire'] = merged_df['code_specialite_partenaire'].astype('category')
   merged_df['code_potentiel'] = merged_df['code_potentiel'].astype('category')
   merged_df['code_statut_partenaire'] = merged_df['code_statut_partenaire'].astype('category')
   merged_df['ville'] = merged_df['ville'].astype('category')
   merged_df['region'] = merged_df['region'].astype('category')
   merged_df['specialite'] = merged_df['specialite'].astype('category')
   merged_df['gamme'] = merged_df['gamme'].astype('category')
   merged_df['etablissement'] = merged_df['etablissement'].astype('category')
   merged_df['flag_accompagnee'] = merged_df['flag_accompagnee'].astype('category')
   merged_df['type_etablissement'] = merged_df['type_etablissement'].astype('category')
   merged_df['role'] = merged_df['role'].astype('category')







   # Convertir les colonnes avec des types de temps en types de données appropriés
   #merged_df['heure_fin_visite'] = pd.to_timedelta(merged_df['heure_fin_visite'])
   merged_df['date_visite'] =   pd.to_datetime(merged_df['date_visite'])
      # close connexion 
   con.close()
   # affichage du résultat
   return merged_df