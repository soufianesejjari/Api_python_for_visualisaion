from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import verify_token


from controllers.Page_performance_controller import Page2Controller
import controllers.Datacontroller as DC
from controllers.Page_principale_controller import Page_principale_controller
from controllers.page_evaluation_controller import Page_Eealuation_controller
from controllers.page_investis_controller import Page_Invest_controller
from controllers.page_partenaire_controller import Page_partenaire_controller
from controllers.Page_user_controller import PageUser
from controllers.Filtrage_controller import Filtrage_controller


from models.Object_model import Object_Model as ObjecModel
from models.Object_model import Object_Invest as Object_Invest
from models.Object_model import Object_Evaluation


app = FastAPI()

DC.schedule_update_data()
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def root():
    return {"message": "Welcome to the API root endpoint."}

@app.post("/endpoint")
def protected_endpoint(token: bool = Depends(verify_token)):
    # Le jeton a été vérifié avec succès, vous pouvez effectuer des opérations ici
    # ...

    return {"message": "Authorized access "}

@app.post("/data")
def get_Data(request: ObjecModel):
    Filtrage_data=Filtrage_controller(DC.data,DC.users).get_filtered_data(request)


    pagePrincipale= Page_principale_controller(Filtrage_data,DC.gammes_uniques,DC.specialites_uniques,DC.regions_uniques,DC.villes_uniques)
    resultats = pagePrincipale.get_principale_data()
    return resultats

@app.post("/performance")
def get_performance(request: ObjecModel): 
    Filtrage_data=Filtrage_controller(DC.data,DC.users).get_filtered_data(request)


    page2_performance = Page2Controller(Filtrage_data)
    resultats = page2_performance.get_page2_data()
    return resultats

@app.post("/partenaire")
def get_partenaire(request: ObjecModel):
    Filtrage_data=Filtrage_controller(DC.data,DC.users).get_filtered_data(request)

    pageParteniare= Page_partenaire_controller(Filtrage_data,DC.gammes_uniques,DC.specialites_uniques,DC.regions_uniques,DC.villes_uniques)
    resultats = pageParteniare.get_partenaire_data()
    return resultats
@app.post("/invest")
def get_Invest(request : Object_Invest):
    Filtrage_data=Filtrage_controller(DC.dataEnvestis,DC.users).get_filtered_Invest(request)

    pageInvest= Page_Invest_controller(Filtrage_data,DC.gammes_uniques,DC.specialites_uniques,DC.regions_uniques,DC.villes_uniques)
    resultats = pageInvest.get_Invest_data()
    return resultats
@app.post("/evaluation")
def get_Evaluation(request : Object_Evaluation):
    Filtrage_data=Filtrage_controller(DC.dataEvaluation,DC.users).get_filtered_Evaluation(request)

    pageEvaluation= Page_Eealuation_controller(Filtrage_data)
    resultats = pageEvaluation.get_evaluation_data()
    return resultats

@app.post("/users")
def get_Users(request: ObjecModel) : 
    Filtrage_data=Filtrage_controller(DC.data,DC.users).get_filtered_data(request)

    pageUsers= PageUser(Filtrage_data,DC.gammes_uniques,DC.specialites_uniques,DC.regions_uniques,DC.villes_uniques)
    resultats = pageUsers.get_user_data()
    return resultats




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
