#Cette fonction initialise la connexion à Google Earth Engine (GEE), 
#en lançant au besoin l’authentification,
#afin de pouvoir accéder aux images Sentinel-2 SR du catalogue GEE.


import ee

def init_gee():
    try:
        ee.Initialize()
        return True
    except Exception:
        ee.Authenticate()
        ee.Initialize()
        return True