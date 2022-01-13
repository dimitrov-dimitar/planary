from resources.auth import Register, Login
from services.plant_id import PlantIdServices

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (PlantIdServices, "/identification"),
)
