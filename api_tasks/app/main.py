from fastapi import FastAPI

from api.api_meetings import meetings_routers
from api.api_tasks import tasks_routers


app = FastAPI()
app.include_router(tasks_routers)
app.include_router(meetings_routers)
