from fastapi import FastAPI

<<<<<<< HEAD
from api.users import user_routers
=======
from app.api.users import user_routers
>>>>>>> 09b7086 (Add user routers)

app = FastAPI()
app.include_router(user_routers)
