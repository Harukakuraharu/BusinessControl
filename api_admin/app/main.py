import sqlalchemy as sa
from admin_panel import admin_panel as sqladmin
from fastapi import FastAPI
from sqladmin import Admin

<<<<<<< HEAD
from api.api_admin import (
=======
from app.api.api_admin import (
>>>>>>> 3f2822f (Complete servis with admin and company)
    admin_routers,
    company_routers,
    organization_routers,
    super_admin_routers,
)
<<<<<<< HEAD
=======

>>>>>>> 3f2822f (Complete servis with admin and company)
from core.settings import config


app = FastAPI()
app.include_router(admin_routers)
app.include_router(super_admin_routers)
app.include_router(company_routers)
app.include_router(organization_routers)


# sqladmin
engine = sa.create_engine(config.dsn)

admin = Admin(
    app,
    engine,
    base_url=f"/{config.ADMIN_PANEL}",
    authentication_backend=sqladmin.authentication_backend,
)
admin.add_view(sqladmin.CompanyAdmin)
admin.add_view(sqladmin.NewsAdmin)
admin.add_view(sqladmin.OrganizationAdmin)
