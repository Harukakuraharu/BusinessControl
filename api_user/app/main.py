from fastapi import FastAPI

<<<<<<< HEAD
<<<<<<< HEAD
from api.users import user_routers
=======
from app.api.users import user_routers
>>>>>>> 09b7086 (Add user routers)
=======
from api.users import user_routers
>>>>>>> 3f2822f (Complete servis with admin and company)

app = FastAPI()
app.include_router(user_routers)
