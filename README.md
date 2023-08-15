

# Project Overview
![image](https://github.com/soufianesejjari/Dynamic-Performance-Analytics-API-Leveraging-MySQL-and-FastAPI/assets/81421925/9f49b8ff-1ccb-4863-a3ee-d7a6f50a4170)

L'API de visites est un service qui permet d'obtenir des données à partir d'une base de données MySQL et d'effectuer des traitements sur ces données pour générer des graphiques dynamiques. L'API utilise également un mécanisme de mise en cache pour optimiser les performances et réduire les requêtes à la base de données.

## Résumé

Le projet consiste à développer une API de visites qui permettra aux utilisateurs d'accéder et d'analyser les données de performance des utilisateurs. L'API se connecte à une base de données MySQL contenant les données de performance et offre des fonctionnalités telles que le filtrage des données, la génération de graphiques dynamiques et l'utilisation d'un mécanisme de mise en cache pour optimiser les performances. Le projet utilise Python comme langage de programmation principal et s'appuie sur le framework FastAPI pour la création d'une API Web rapide et évolutive

## Objectifs du projet

* Fournir une interface API permettant aux utilisateurs d'accéder aux données de performance des utilisateurs.
    
* Permettre aux utilisateurs de filtrer les données en fonction de différents critères tels que l'ID de l'utilisateur, l'ID du responsable, l'année, le mois, la gamme des partenaires et la région.
    
* Générer des graphiques dynamiques à partir des données filtrées pour une visualisation claire et concise des performances.
    
* Utiliser un mécanisme de mise en cache pour optimiser les performances et minimiser les requêtes à la base de données.
    

## Technologies utilisées

* Python : Utilisé comme langage de programmation principal pour la logique de l'API.
    
* FastAPI : Un framework Python pour la création d'API Web rapides et évolutives.
    
* MySQL : Une base de données relationnelle utilisée pour stocker les données de performance des utilisateurs.
    
* Pandas : Une bibliothèque Python pour la manipulation et l'analyse des données.
    

## Fonctionnalités principales

1. Récupération des données : L'API permet aux utilisateurs de récupérer les données à partir de la base de données MySQL.
    
2. Filtrage des données : Les utilisateurs peuvent filtrer les données en spécifiant différents critères tels que l'ID de l'utilisateur, l'ID du responsable, l'année, le mois, la gamme des partenaires et la région.
    
3. Mise en cache des données : Les résultats des requêtes fréquentes sont mis en cache , ce qui permet de réduire les temps de réponse et les requêtes à la base de données.
    
4. Sécurité : L'API met en œuvre un mécanisme d'authentification basé sur des tokens pour sécuriser l'accès aux données.
    

## Exigences

L'API de visites nécessite Python 3.6 ou une version ultérieure.

De plus, elle utilise les bibliothèques suivantes :

* pandas : Une bibliothèque Python utilisée pour la manipulation et l'analyse des données.
    
* fastapi : Un framework Python pour la création d'API Web rapides et évolutives.
    
* sqlalchemy : Une bibliothèque Python qui facilite l'interaction avec les bases de données relationnelles.
    
* uvicorn : Un serveur ASGI qui permet d'exécuter l'API
    

## structure de projet

```javascript
├── app.py
├── auth.py
├── config
│   └── config.py
├── controllers
│   ├── Datacontroller.py
│   ├── Filtrage_controller.py
│   ├── Page_performance_controller.py
│   ├── Page_principale_controller.py
│   ├── Page_evaluation_controller.py
│   ├── Page_investis_controller.py
│   ├── Page_partenaire_controller.py
│   └── Page_user_controller.py
├── models
│   ├── Principale_model.py
│   ├── Evaluation_model.py
│   └── Investis_model.py
│   └── Object_model.py
├── requirements.txt
└── root
    └── root.py
```

Explication de la structure du projet :

* **app.py**: C'est le fichier principal qui exécute l'API. Il est responsable du lancement de l'application FastAPI et du montage des différents points d'accès.
    
* **auth.py**: C'est le fichier qui gère l'authentification et l'autorisation des utilisateurs de l'API. Il contient les fonctions et les mécanismes nécessaires pour sécuriser l'accès aux données.
    
* **config**: Ce dossier contient le fichier config.py qui contient les configurations de l'API, telles que les informations **de connexion à la base de données**, le **délai** de mis a jour, etc.
    
* **controllers**: Ce dossier contient les différents contrôleurs de l'API. Chaque contrôleur est responsable de la logique métier liée à un aspect spécifique de l'API. Les contrôleurs importent les modèles nécessaires et utilisent les données pour générer les résultats souhaités.
    
* **models**: Ce dossier contient les modèles de données utilisés par les contrôleurs. Chaque modèle représente une structure de données spécifique et contient des méthodes pour manipuler ces données.
    
* **root**: Ce dossier contient le fichier root.py qui gère les points d'accès de l'API racine. Il fait le lien avec les différents contrôleurs pour fournir les résultats attendus.
    
* **requirements.txt**: Ce fichier contient la liste des dépendances requises par l'API. Vous pouvez l'utiliser avec la commande pip install -r requirements.txt pour installer toutes les dépendances nécessaires.
    

## Installation et Démarrage

Pour installer et exécuter l'API de visites, suivez les étapes ci-dessous :

1. Assurez-vous que vous avez Python 3.6 ou une version ultérieure installée sur votre machine.
    
2. Accédez au répertoire du projet : cd mediviz-data/dev
    

Installez les dépendances requises à l'aide de pip et du fichier requirements.txt :

pip install -r requirements.txt

Cela installera les bibliothèques Python nécessaires telles que Pandas, SQLAlchemy, Flask, etc.

1. Configurez les paramètres de l'API en éditant le fichier config/config.py. Assurez-vous de fournir les informations de connexion appropriées à votre base de données MySQL et d'autres paramètres de configuration nécessaires.
    
    ```python
    DB_USER = "root"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_NAME = "dev_crm_health"
    ```
    
2. Exécutez l'API à l'aide de la commande suivante :
    
    python app.py  
    Si tout se passe bien, vous verrez quelque chose comme ça dans votre console de serveur:
    
    ```javascript
    Data updated at 2023-05-26 14:10:07.641934
    INFO:     Started server process [25448]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
    ```
    
    Cela lancera l'API sur votre machine locale avec l'hôte localhost et le port 8000.
    
3. Vous pouvez maintenant accéder à l'API de visites à l'adresse suivante :
    
    http://localhost:8000
    

## Les paramètres de L’API

Voici les paramètres de filtrage utilisés dans le contrôleur Filtrage\_controller pour /pertenaire /data /performance et leur description :

| Paramètre | Type | Description |
| --- | --- | --- |
| id\_responsable | int | ID du responsable. |
| id\_utilisateur | int | ID de l'utilisateur. |
| annee | int | Année de la visite. |
| mois | int | Mois de la visite. |
| gamme | str | Gamme des partenaires. |
| region | str | Région des partenaires. |
| start\_date | datetime.date | Date de début de la période spécifiée. |
| end\_date | datetime.date | Date de fin de la période spécifiée. |

Le contrôleur Filtrage\_controller utilise ces paramètres pour filtrer les données en fonction des critères spécifiés.

Voici un exemple de l'objet qui contient les paramètres de filtrage :

```python
filters={
    "id_responsable": 1,
    "id_utilisateur": 2,
    "annee": 2023,
    "mois": 5,
    "gamme": "A",
    "region": "Europe",
    "start_date": "2023-05-01",
    "end_date": "2023-05-15"
}
```

Vous pouvez utiliser cet objet dans votre appel à l'API pour spécifier les critères de filtrage.

Voici un exemple de code utilisant la bibliothèque pandas pour effectuer le filtrage sur un DataFrame :

```python
import pandas as pd

# Supposons que vous ayez un DataFrame nommé "data" contenant les données initiales
data= data[data['id_utilisateur'] == int(id_utilisateur)]
data= self.df[data['date_visite'].dt.year == int(annee)]
```

Dans cet exemple, le DataFrame initial "data" est filtré en fonction des critères spécifiés dans l'objet filters. Chaque condition de filtrage est appliquée en utilisant les opérations de comparaison appropriées. Le DataFrame filtré est stocké dans la variable filtered\_data, et vous pouvez effectuer d'autres opérations ou analyses sur ce DataFrame selon vos besoins.

## Points de Terminaison de l'API

avans de parlé sur les points de terminaision en va parlé sur

L'API de visites propose plusieurs points de terminaison pour récupérer différentes informations sur les visites effectuées. Voici les détails des endpoints disponibles :

### Endpoint : /data

| **API endpoint** | **Description** | **Method** | Paramètres |
| --- | --- | --- | --- |
| http://localhost:8000/data | Récupère les données de visite filtrées en fonction des paramètres spécifiés. | POST | tous qui sont dans la section paramètres |

Voici un extrait de code pour le traitement effectué dans le contrôleur de cet endpoint :

```python
import pandas as pd
class Page_principale_controller:
    # ...
    def get_principale_data(self):
        # ...
        return finaleDic
    def getRegionDic(self, df, regions_uniques, villes_uniques):
        # ...
    def getGammeDic(self, df, gammes_uniques, specialites_uniques):
        # ...
    def getStat(self, df):
        # ...
```

Dans cet exemple, la méthode get\_principale\_data effectue le traitement principal pour obtenir les données de la page principale. Elle appelle les méthodes auxiliaires getRegionDic, getGammeDic, et getStat pour obtenir les statistiques spécifiques et les données filtrées par région et par gamme .

### Structure de la réponse

La réponse renvoie un dictionnaire contenant les résultats des données principales, regroupés par différentes catégories.

Voici la structure de la réponse :

```python
{
  "statistiques": {},
  "region": [],
  "gammes": []
}
```

* "statistiques" : Cette section contient des statistiques globales sur les visites, telles que le nombre total de visites planifiées, non planifiées, médicales, pharmaceutiques, privées et publiques, ainsi que le nombre de visites selon le type d'établissement et le type de visite.
    
* "region" : Cette section contient des informations sur les régions partenaires. Chaque élément de la liste représente une région avec les détails suivants :
    
    * "code\_region\_partenaire" : Code de la région partenaire
        
    * "region" : Nom de la région
        
    * "nb\_visites\_total" : Nombre total de visites dans la région
        
    * "ville" : Liste des villes de la région avec les détails suivants :
        
        * "code\_ville\_partenaire" : Code de la ville partenaire
            
        * "code\_region\_partenaire" : Code de la région partenaire
            
        * "ville" : Nom de la ville
            
        * "region" : Nom de la région associée à la ville
            
        * "nb\_visites" : Nombre de visites dans la ville
            
* "gammes" : Cette section contient des informations sur les gammes de partenaires. Chaque élément de la liste représente une gamme avec les détails suivants :
    
    * "code\_gamme" : Code de la gamme
        
    * "gamme" : Nom de la gamme
        
    * "nbr\_total\_visites" : Nombre total de visites dans la gamme
        
    * "specialites" : Liste des spécialités de la gamme avec les détails suivants :
        
        * "code\_specialite" : Code de la spécialité
            
        * "specialite" : Nom de la spécialité
            
        * "gamme" : Nom de la gamme associée à la spécialité
            
        * "code\_gamme" : Code de la gamme associée à la spécialité
            
        * "nb\_visites\_total" : Nombre de visites pour cette spécialité dans la gamme
            

### Exemple de calcul des résultats

Le code utilise des opérations de regroupement (groupby) pour calculer les résultats en fonction des filtres appliqués aux données principales.

Voici un exemple de calcul pour la catégorie "region" :

```python
visites_par_region_ville = df.groupby(['region', 'ville'])['id_visite'].count().reset_index().rename(columns={'id_visite': 'nb_visites'})
visites_par_region = visites_par_region_ville.groupby(['region'])['nb_visites'].sum().reset_index().rename(columns={'nb_visites': 'total_visites'})
.....

for _, row in resultat.iterrows():
    region = row['region']
    code_region_partenaire = row['code_region_partenaire']
    ville = row['ville']
    code_ville_partenaire = row['code_ville_partenaire']
    nb_visites = row['nb_visites']
    total_visites = row['total_visites']
    index = None
    for i, result in enumerate(resultats):
        if result['region'] == region:
            index = i
            break

    if index is None:
        resultats.append({
            'code_region_partenaire': code_region_partenaire,
            'region': region,
            "nb_visites_total": total_visites,
            "ville": []
        })
        index = len(resultats) - 1

    if nb_visites > 0:
        resultats[index]["ville"].append({
            'code_ville_partenaire': code_ville_partenaire,
            'code_region_partenaire': code_region_partenaire,
            "ville": ville,
            "region": region,
            "nb_visites": nb_visites
        })

return resultats
```

Dans cet exemple, les données sont regroupées par région et ville pour compter le nombre de visites. Ensuite, les résultats sont fusionnés avec les données uniques de villes et de régions pour obtenir les informations complètes. En parcourant les lignes du résultat final, une liste de résultats est construite, avec chaque élément contenant les détails de la région, y compris une liste de villes associées avec le nombre de visites correspondant.

Les autres catégories de résultats suivent une logique similaire, utilisant des opérations de regroupement pour calculer les statistiques et construire la structure de réponse appropriée.

Exemple:

Body:

```python
{
    "id_responsable" : 25,
    "start_date": "2023-01-01",
    "end_date": "2023-03-01"
}
```

Resultat de l’api:

```python
{
    "statistiques": {
        "nbr_total_visites_non_planifiees": 17322,
        "nbr_total_visites_planifiees": 558,
        "nbr_visites_medicales_non_planifiees": 15012,
        "nbr_visites_pharmaceutiques_non_planifiees": 2306,
        "nbr_visites_medicales_planifiees": 558,
        "nbr_visites_pharmaceutiques_planifiees": 0,
        "nbr_visites_privees_non_planifiees": 8813,
        "nbr_visites_publiques_non_planifiees": 6199,
        "nbr_visites_privees_planifiees": 389,
        "nbr_visites_publiques_planifiees": 169,
        "nbr_visites_groupe_non_planifiees": 979,
        "nbr_visites_simple_non_planifiees": 16343,
        "nbr_visites_groupe_planifiees": 8,
        "nbr_visites_simple_planifiees": 550,
        "nbr_visites_indiviuel_non_planifiees": 16970,
        "nbr_visites_en_double_non_planifiees": 352,
        "nbr_visites_indiviuel_planifiees": 557,
        "nbr_visites_en_double_planifiees": 1,
        "region": [
            {
                "code_region_partenaire": "RE00002",
                "region": "Casablanca",
                "nb_visites_total": 4113,
                "ville": [
                    {
                        "code_ville_partenaire": "VI00019",
                        "code_region_partenaire": "RE00002",
                        "ville": "Azemmour",
                        "region": "Casablanca",
                        "nb_visites": 7
                    },
                   ...........
        ],
        "gammes": [
            {
                "code_gamme": "GA00001",
                "gamme": "DERMATO",
                "nbr_total_visites": 219,
                "specialites": [
                    {
                        "code_specialite": "SP00001",
                        "specialite": "Chirurgie Plastique",
                        "gamme": "DERMATO",
                        "code_gamme": "GA00001",
                        "nb_visites_total": 68
                    },
                    
                    ............
    }
}
```

Dans cet exemple de résultat, vous pouvez voir les statistiques générales, les gammes avec leurs spécialités correspondantes, et les régions avec leurs villes correspondantes, le tout au format JSON

### Endpoint : /performance

Cet endpoint permet d'obtenir des données de performance basées sur les visites des partenaires. Voici comment appeler cet endpoint et la méthode associée :

| **API endpoint** | **Method** | Paramètres |
| --- | --- | --- |
| http://localhost:8000/performance | POST | tous qui sont dans la section paramètres |

Le code du contrôleur Page2Controller fournit une méthode get\_page2\_data qui effectue le traitement pour obtenir les données de performance. Les données sont regroupées en fonction de différents critères tels que le type de compte, le statut, la région, l'utilisateur, le délégué, le jour et le potentiel.

Le traitement se fait comme suit (des extraits ) :

1. Groupement des données par type de compte :
    
    ```python
    groupe_type_compte = self.df.groupby('code_type_partenaire')['id_visite'].nunique().reset_index()
    ```
    
    Ici, les données sont regroupées par le code du type de compte, et le nombre de visites uniques est calculé pour chaque type de compte.
    
2. Groupement des données par utilisateur (les 5 utilisateurs avec le plus grand nombre de visites) :
    
    ```python
    groupe_utilisateur = self.df.groupby('fullName_utilisateur')['id_visite'].nunique().nlargest(5).reset_index()
    ```
    
    Les données sont regroupées par nom d'utilisateur, et les 5 utilisateurs avec le plus grand nombre de visites uniques sont sélectionnés.
    

### Structure de la réponse

La réponse renvoie un dictionnaire contenant les résultats des performances de la page 2, regroupés par différentes catégories.

Voici la structure de la réponse :

```python
{
  "nombre_compte_visite_par_type_compte": [],
  "nombre_compte_visite_par_status": [],
  "nombre_visites_par_potenciel": [],
  "nombre_visites_par_region": [],
  "utilisateurs_plus_grand_nombre_visites": [],
  "delegues_moins_nombre_visites": [],
  "nombre_compte_visite_par_jour": []
}
```

Chaque catégorie de résultats contient une liste d'éléments avec des informations spécifiques.

* nombre\_compte\_visite\_par\_type\_compte: Résultats du nombre de visites par type de compte, contenant le code du type de compte et le nombre de visites correspondant.
    
* nombre\_compte\_visite\_par\_status: Résultats du nombre de visites par statut de compte, contenant le code du statut de compte et le nombre de visites correspondant.
    
* nombre\_visites\_par\_potenciel: Résultats du nombre de visites par potentiel, contenant le code du potentiel et le nombre de visites correspondant.
    
* nombre\_visites\_par\_region: Résultats du nombre de visites par région, contenant le nom de la région et le nombre de visites correspondant.
    
* utilisateurs\_plus\_grand\_nombre\_visites: Résultats des utilisateurs avec le plus grand nombre de visites, contenant le nom de l'utilisateur et le nombre de visites correspondant.
    
* delegues\_moins\_nombre\_visites: Résultats des délégués avec le moins de visites, contenant le nom du délégué et le nombre de visites correspondant.
    
* nombre\_compte\_visite\_par\_jour: Résultats du nombre de visites par jour, contenant la date de la visite et le nombre de visites correspondant.
    

Exemple:

Body: Resultat de l’api:

```python
{
    "id_responsable" : 25,
    "annee": "2023",
   "region" : RE00001
}
```

```python
{
    "nombre_compte_visite_par_type_compte": [

        {
            "code_type_partenaire": "MEDE",
            "nombre_visites": 2
        }..
    ],
    "nombre_compte_visite_par_status": [
        {
            "code_statut_partenaire": "VALI",
            "nombre_visites": 2
        }
    ],
    "nombre_visites_par_potenciel": [
    
        {
            "code_potentiel": "A",
            "nombre_visites": 1
        },
      
        ....
    ],
    "nombre_visites_par_region": [
        {
            "region": "Agadir",
            "nombre_visites": 2
        }...
    ],
    "utilisateurs_plus_grand_nombre_visites": [
        {
            "delegue": "AZAROUAL BACHIR",
            "nombre_visites": 1
        }...
    "delegues_moins_nombre_visites": [
        {
            "COALESCE(tv.id_responsable, 0)": 25,
            "delegue": 1
        }...
    ],
    "nombre_compte_visite_par_jour": [
        {
            "date_visite": "2023-01-05",
            "nombre_visites": 1
        }....
    ]
}
```

Dans cet exemple de résultat, vous pouvez voir les différentes statistiques de performance obtenues à partir des visites des partenaires, telles que le nombre de visites par type de compte, par statut, par potentiel, par région, par utilisateur, par délégué et par jour.

## Endpoint /partenaire

Cet endpoint permet d'obtenir des informations sur les partenaires en fonction des paramètres spécifiés.

| **API endpoint** | **Method** | Paramètres |
| --- | --- | --- |
| http://localhost:8000/partenaire | POST | tous qui sont dans la section paramètres |

### Structure de la réponse

La réponse renvoie un dictionnaire contenant les résultats des partenaires, regroupés par différentes catégories.

Voici la structure de la réponse :

```python
{
  "Nombre_de_comptes_par_potentiel": [],
  "Nombre_de_visites_moyen": 0,
  "Nombre_de_comptes_par_etablissement": [],
  "region_partenaire": [],
  "gamme_partenaire": []
}
```

Chaque catégorie de résultats contient une liste d'éléments avec des informations spécifiques.

* Nombre\_de\_comptes\_par\_potentiel: Nombre de comptes de partenaires regroupés par potentiel d'investissement.
    
* Nombre\_de\_visites\_moyen: Nombre moyen de visites par compte de partenaire.
    
* Nombre\_de\_comptes\_par\_etablissement: Nombre de comptes de partenaires regroupés par établissement.
    
* region\_partenaire: Résultats regroupés par région, contenant le nombre de partenaires par région et par ville.
    
* gamme\_partenaire: Résultats regroupés par gamme, contenant le nombre de partenaires par gamme et par spécialité.
    

Chaque élément de ces catégories contient des informations spécifiques, telles que le potentiel, le nombre de visites moyen, l'établissement, la région, la ville, la gamme, la spécialité, le code de la gamme et le code de la spécialité.

### Exemple de calcul des résultats

Le code utilise des opérations de regroupement (groupby) pour calculer les résultats en fonction des filtres appliqués aux données des partenaires.

Voici un exemple de calcul pour la catégorie "Nombre de comptes par potentiel" :

```python
comptes_potentiel = df.groupby("code_potentiel")["id_partenaire"].nunique().reset_index().rename(columns={'id_partenaire': 'nombre_partenaire'})
```

Dans cet exemple, nous regroupons les données des partenaires par le code de potentiel, puis comptons le nombre de comptes de partenaires correspondants.

Les autres catégories de résultats sont calculées de manière similaire en utilisant les colonnes appropriées pour le regroupement et le calcul des sommes ou des moyennes.

Exemple:

Body: Resultat de l’api:

```python
{
    "id_responsable": 25,
    "annee": "2023",
    "region": "RE00001"
}
```

```python
{
    "Nombre_de_comptes_par_potentiel": [
        {
            "code_potentiel": " B",
            "nombre_partenaire": 0
        }.........
    ],
    "Nombre_de_visites_moyen": 1.9155778894472362,
    "Nombre_de_comptes_par établissement": [
        {
            "etablissement": "Cabinet",
            "nombre_partenaire": 814
        },
        ..........
    ],
    "region_partenaire": [
        {
            "code_region_partenaire": "RE00001",
            "region": "Agadir",
            "total_partenaire": 247,
            "ville": [
                {
                    "code_ville_partenaire": "VI00001",
                    "code_region_partenaire": "RE00001",
                    "ville": "Agadir",
                    "region": "Agadir",
                    "nb_partenaire": 111
               .........
            ]
        }
    ],
    "gamme_partenaire": [
        {
            "code_gamme": "GA00001",
            "gamme": "DERMATO",
            "total_partenaire": 18,
            "specialites": [
                {
                    "code_specialite": "SP00002",
                    "specialite": "Dermatologie",
                    "gamme": "DERMATO",
                    "code_gamme": "GA00001",
                    "nb_partenaire": 18
            ...........    }
            
            ]
        }
    ]
}
```

La réponse finale contient les différentes statistiques demandées, telles que le nombre de comptes par potentiel, le nombre moyen de visites par partenaire, le nombre de comptes par établissement, les régions des partenaires avec le nombre de partenaires par région et par ville, ainsi que les gammes des partenaires avec le nombre de partenaires par gamme et par spécialité.

## Endpoint /evaluation

Cet endpoint permet d'obtenir les données d'évaluation à partir du DataFrame fourni et returne des statistique sur les evaluation.

| **API endpoint** | **Method** | Paramètres |
| --- | --- | --- |
| http://localhost:8000/partenaire | POST | Filtrage par id\_utilisateur : Garde les lignes où l'ID de l'utilisateur correspond à id\_utilisateur. |

### Structure de la réponse

* Nombre de visites par rapport au moyen d'évaluation: Un dictionnaire indiquant le nombre de visites en fonction du moyen d'évaluation utilisé. Les clés représentent les moyens d'évaluation (par exemple, "Mauvais", "Moyen", "Bon") et les valeurs représentent le nombre de visites correspondant à chaque moyen.
    
* Nombre d'évaluation par Mois: Un dictionnaire indiquant le nombre d'évaluations effectuées par mois. Les clés sont des chaînes de caractères au format "YYYY-MM" représentant le mois, et les valeurs représentent le nombre d'évaluations effectuées ce mois-là.
    
* Pourcentage d'évaluations par rôle: Un dictionnaire indiquant le pourcentage d'évaluations effectuées par rôle. Les clés sont les rôles (par exemple, "Médecin", "Pharmacien") et les valeurs représentent le pourcentage d'évaluations effectuées par ce rôle.
    
* Moyenne de points\_obtenus par les utilisateurs: Un dictionnaire indiquant la moyenne des points obtenus par utilisateur. Les clés sont les noms des utilisateurs et les valeurs représentent la moyenne des points obtenus par cet utilisateur.
    
* categories: Une liste d'objets représentant les catégories évaluées. Chaque objet contient les informations suivantes :
    
    * code\_categorie: Le code de la catégorie.
        
    * categorie: Le nom de la catégorie.
        
    * moyenne\_points\_categorie: La moyenne des points obtenus pour cette catégorie.
        
    * sous\_categories: Une liste d'objets représentant les sous-catégories évaluées dans cette catégorie. Chaque objet contient les informations suivantes :
        
        * code\_sous\_categorie: Le code de la sous-catégorie.
            
        * sous\_categorie: Le nom de la sous-catégorie.
            
        * moyenne\_points\_sous\_categorie: La moyenne des points obtenus pour cette sous-catégorie.
            

### Calcul des résultats

Les résultats sont calculés à partir des données fournies dans le DataFrame df.

* get\_evaluation\_data: Cette méthode appelle les autres méthodes pour obtenir les différentes parties des résultats et les regroupe dans un dictionnaire final.
    
* getCategoriesDic: Cette méthode extrait les catégories et les sous-catégories uniques du DataFrame. Ensuite, elle calcule les moyennes des points obtenus pour chaque catégorie et sous-catégorie. Les résultats sont stockés dans une liste d'objets avec les informations nécessaires.
    
* getStatEvakuation: Cette méthode calcule les statistiques générales telles que le nombre de visites par rapport au moyen d'évaluation, le nombre d'évaluations par mois, le pourcentage d'évaluations par rôle et la moyenne des points obtenus par utilisateur.
    
    * exemple de le nombre d'évaluations par mois :  evaluations\_mois = df.groupby(df\["date\_integration"\].dt.strftime("%Y-%m"))\["point\_Detail"\].count().to\_dict()
        

Exemple:

```python
{
    "code_categorie": "CE00005",
    "id_utilisateur": "49"
}
```

```python
{
    "Nombre_visites_par_moyen_evaluation": [
        {
            "points_obtenus": 62,
            "nombre_visites": 55700
        },
 .....
    ],
    "Nombre_evaluation_par_Mois": [
        {
            "date_integration": "2023-03",
            "Nombre_evaluation": 25
        },
....
    ],
    "pourcentage_evaluations_role": [
        {
            "role_createur": "DIR",
            "Nombre_evaluation": 25
        },
......
    ],
    "moyenne_points_utilisateurs": [
        {
            "FullName_utilisateur": "AGHZAF ABOU",
            "points_obtenus": 62.0
        },
....
    ],
    "categories": [
        {
            "code_categorie": "CE00005",
            "categorie": "Preparation de la visite ",
            "moyenne_points_categorie": 65.0,
            "sous_categories": [
                {
                    "code_sous_categorie": "SEV00016",
                    "sous_categorie": "Plannification semaine de travail sur CRM ",
                    "moyenne_points_sous_categorie": 1.3333333333333333
                },.......
```

## Endpoint /invest

Cet endpoint permet d'obtenir les données d'investissement filtrées en fonction des paramètres spécifiés.

| **API endpoint** | **Method** | Paramètres |
| --- | --- | --- |
| http://localhost:8000/invest | POST | Filtrage par id\_responsable |

### Structure de la réponse

La réponse renvoie un dictionnaire contenant les résultats de l'investissement, regroupés par différentes catégories.

Voici la structure de la réponse :

```python
{
  "budget_par_visites": [],
  "budget_par_gamme": [],
  "budget_par_statut": [],
  "budget_par_potentiel": [],
  "budget_par_specialite": [],
  "budget_par_region": [],
  "budget_par_type_investissement": [],
  "budget_par_categorie_investissement": []
}
```

Chaque catégorie de résultats contient une liste d'éléments avec des informations spécifiques.

* budget\_par\_visites: Budgets groupés par nombre de visites.
    
* budget\_par\_gamme: Budgets groupés par gamme d'investissement.
    
* budget\_par\_statut: Budgets groupés par statut d'investissement.
    
* budget\_par\_potentiel: Budgets groupés par potentiel d'investissement.
    
* budget\_par\_specialite: Budgets groupés par spécialité.
    
* budget\_par\_region: Budgets groupés par région.
    
* budget\_par\_type\_investissement: Budgets groupés par type d'investissement.
    
* budget\_par\_categorie\_investissement: Budgets groupés par catégorie d'investissement.
    

Chaque élément de ces catégories contient des informations spécifiques, telles que le nombre de visites, la gamme, le statut, le potentiel, la spécialité, la région, le type d'investissement et la catégorie d'investissement, ainsi que le budget total associé.

### Exemple de calcul des résultats

La méthode getInvis est responsable du calcul des résultats en fonction des filtres appliqués aux données d'investissement.

Elle utilise des opérations de regroupement (groupby) et de calcul (sum) pour obtenir les sommes des budgets correspondantes.

Voici un exemple de calcul pour la catégorie "budget\_par\_gamme" :

```javascript
budget_par_gamme = df.groupby('code_gamme')['budget'].sum().reset_index()
budget_par_gamme = budget_par_gamme.merge(gamme, left_on='code_gamme', right_on='code_gamme_partenaire', how='left')
```

Dans cet exemple, nous regroupons les données d'investissement par le code de la gamme, puis calculons la somme des budgets correspondants.

Ensuite, nous fusionnons les résultats avec les informations de la gamme à l'aide de la colonne "code\_gamme\_partenaire" pour obtenir des détails supplémentaires sur chaque gamme.

Les autres catégories de résultats sont calculées de manière similaire en utilisant les colonnes appropriées pour le regroupement et le calcul des sommes.

Exemple

```python
{
    "id_responsable": 20,
    "code_type_investissement": "TI00001"
}
```

```python
{
    "budget_par_visites": [
        {
            "Nombre de nombre de visites": 0.0,
            "budget": 6000
        }......
      
    ],
    "budget_par_gamme": [
        {
            "code_gamme": "GA00002",
            "budget": 12000,
            "gamme": "GYNECO"
     } ...
    ],
    "budget_par_statut": [
        {
            "code_statut_bc": "ANNU",
            "budget": 10000
        }.....
     
    ],
    "budget_par_potentiel": [
        {
            "code_potentiel": "A",
            "budget": 32000
        }
    ],
    "budget_par_specialite": [
        {
            "code_specialite": "SP00006",
            "budget": 13000,
            "specialite": "Médecine Générale"
        }
    ],
    "budget_par_region": [
        {
            "code_region_partenaire": "RE00002",
            "budget": 50000,
            "region": "Casablanca"
        }
    ],
    "budget_par_type_investissement": [
        {
            "code_type_investissement": "TI00001",
            "budget": 18000
        }
    ],
    "budget_par_categorie_investissement": [
        {
            "code_categorie_investissement": "CI00003",
            "budget": 12000
        }
```

## Endpoint /users

Cet endpoint permet d'obtenir les données d'investissement filtrées en fonction des paramètres spécifiés.

| **API endpoint** | **Method** | Paramètres |
| --- | --- | --- |
| http://localhost:8000/users | POST | tous qui sont dans la section paramètres |

### Structure de la réponse

La réponse renvoie un dictionnaire contenant les résultats des informations sur les utilisateurs, regroupés par différentes catégories.

Voici la structure de la réponse :

```python
{
  "nombre_nouvelle_utilisateur_par_mois": [],
  "nombre_utilisateur_par_gammes": [],
  "pourcentage_visites_par_responsable": [],
  "nombre_utilisateur_par_regions": [],
  "nombre_utilisateur_par_status": [],
  "nombre_utilisateur_par_role": []
}
```

Chaque catégorie de résultats contient une liste d'éléments avec des informations spécifiques.

* nombre\_nouvelle\_utilisateur\_par\_mois: Résultats du nombre de nouveaux utilisateurs par mois, contenant le mois et le nombre d'utilisateurs correspondant.
    
* nombre\_utilisateur\_par\_gammes: Résultats du nombre d'utilisateurs par gamme, contenant le code de la gamme et le nombre d'utilisateurs correspondant.
    
* pourcentage\_visites\_par\_responsable: Résultats du pourcentage de visites par responsable, contenant l'ID du responsable et le nombre de visites correspondant.
    
* nombre\_utilisateur\_par\_regions: Résultats du nombre d'utilisateurs par région, contenant le nom de la région et le nombre d'utilisateurs correspondant.
    
* nombre\_utilisateur\_par\_status: Résultats du nombre d'utilisateurs par statut, contenant le code du statut et le nombre d'utilisateurs correspondant.
    
* nombre\_utilisateur\_par\_role: Résultats du nombre d'utilisateurs par rôle, contenant le nom du rôle et le nombre d'utilisateurs correspondant.
    

Chaque élément de ces catégories contient des informations spécifiques correspondant à chaque catégorie.

Exemple

```python
{
    "id_responsable": 25
}
```

```python
{
    "nombre_nouvelle_utilisateur_par_mois": [
        {
            "mois": 1,
            "nombre_utilisateur": 51
       ........
    ],
    "nombre_utilisateur_par_gammes": [
        {
            "code_gamme": "GA00001",
            "nombre_utilisateur": 11
    
    ],

    "nombre_utilisateur_par_regions": [
        {
            "region": "Agadir",
            "nombre_utilisateur": 3
    .......
    ],
    "nombre_utilisateur_par_status": [
        {
            "code_statut_partenaire": "VALI",
            "nombre_utilisateur": 54
        }
    ],
    "nombre_utilisateur_par_role": [
        {
            "role": "DEL",
            "nombre_utilisateur": 48
...... 
        }
    ]
}
```

# Conclusion :

Le projet de l'API de visites a été développé avec succès pour fournir une interface permettant aux utilisateurs d'accéder aux données de performance des utilisateurs. L'API offre des fonctionnalités telles que la récupération de données, le filtrage des données, la génération de graphiques dynamiques, et l'utilisation d'un mécanisme de mise en cache pour optimiser les performances.

La technologie principale utilisée dans ce projet est Python, avec le framework FastAPI pour la création d'API Web rapides et évolutives. La base de données MySQL est utilisée pour stocker les données de performance des utilisateurs, et la bibliothèque Pandas est utilisée pour la manipulation et l'analyse des données.

L'API est configurée à l'aide du fichier de configuration [config.py](http://config.py), où les informations de connexion à la base de données et d'autres paramètres sont spécifiés. L'authentification des utilisateurs est gérée par le fichier [auth.py](http://auth.py), qui met en place un mécanisme d'authentification basé sur des tokens pour sécuriser l'accès aux données.

Le projet est organisé en plusieurs dossiers et fichiers, tels que [app.py](http://app.py) pour le lancement de l'API, les contrôleurs pour la logique métier, les modèles de données pour la représentation des données, et le dossier de configuration pour les paramètres de l'API. Un fichier requirements.txt est fourni pour installer les dépendances nécessaires.

Les points de terminaison de l'API comprennent la récupération de données, la performance et les informations sur les partenaires. Chaque point de terminaison accepte des paramètres de filtrage pour obtenir les résultats souhaités.

En conclusion, le projet de l'API de visites a réussi à fournir une solution efficace pour accéder et analyser les données de performance des utilisateurs. Il offre une interface conviviale et des fonctionnalités avancées pour la visualisation des données. Le projet est extensible et peut être adapté pour répondre aux besoins spécifiques des utilisateurs.


# Références
Les références ci-dessous ont été utilisées pour le développement du projet API de Visites pour l'Analyse des Performances des Utilisateurs :

- FastAPI Documentation: Documentation officielle du framework FastAPI, qui a été utilisé pour créer l'API Web.

- Pandas Documentation: Documentation officielle de la bibliothèque Pandas, utilisée pour la manipulation et l'analyse des données.

- MySQL Documentation: Documentation officielle de MySQL, utilisée pour l'interaction avec la base de données MySQL.

- SQLAlchemy Documentation: Documentation officielle de SQLAlchemy, une bibliothèque Python qui facilite l'interaction avec les bases de données relationnelles.

- Uvicorn Documentation: Documentation officielle d'Uvicorn, un serveur ASGI utilisé pour exécuter l'API.

- Python Official Website: Site web officiel de Python, le langage de programmation utilisé pour le développement du projet.

- OpenAI GPT-3.5 Documentation: Documentation officielle d'OpenAI pour GPT-3.5, le modèle utilisé pour fournir des réponses et des explications.
