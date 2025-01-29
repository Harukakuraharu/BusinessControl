from fastapi import FastAPI

<<<<<<< HEAD
from api.api_meetings import meetings_routers
from api.api_tasks import tasks_routers


app = FastAPI()
app.include_router(tasks_routers)
app.include_router(meetings_routers)
=======

app = FastAPI()
>>>>>>> d0ff108 (Added new servise)
