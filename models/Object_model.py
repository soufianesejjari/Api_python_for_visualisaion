from pydantic import BaseModel


class Object_Model(BaseModel):
    id_utilisateur: int = None
    id_responsable: int = None
    annee: int = None
    mois: int = None
    gamme: str = None
    region: str = None
    start_date: str = None
    end_date: str = None

    #model d object d'inevst 
class Object_Invest(BaseModel):
    id_partenaire: int = None
    id_responsable: int = None
    id_business_case : int =None
    code_type_investissement : str =None


    region: str = None
    start_date: str = None
    end_date: str = None
    #model d object d'inevst 
class Object_Evaluation(BaseModel):
    id_utilisateur: str = None
    code_categorie: str = None
    start_date: str = None
    end_date: str = None

