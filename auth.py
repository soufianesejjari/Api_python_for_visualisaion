from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Vérifiez ici la validité du jeton
    # Vous pouvez utiliser des bibliothèques telles que PyJWT pour déchiffrer et valider le jeton

    # Exemple de vérification de jeton bidon
    if credentials.scheme == "Bearer" and credentials.credentials == "mediviz":
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid token")
