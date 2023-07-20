import sqlalchemy as db

# Configuration de la base de données MySQL
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_NAME = "dev_crm_health"

# Création d'un moteur de connexion à la base de données MySQL
engine = db.create_engine(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=True)

# Connexion à la base de données MySQL
connection = engine.connect()


# temps de mis a jour par secondes
timeMis=100
