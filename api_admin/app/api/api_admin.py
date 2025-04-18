from fastapi.routing import APIRouter
from services import admin_services

from core import dependency
from schemas import schemas


admin_routers = APIRouter(prefix="/admin", tags=["Admin"])
super_admin_routers = APIRouter(prefix="/super_admin", tags=["SuperAdmin"])

company_routers = APIRouter(
    prefix="/company",
    tags=["Company"],
)

organization_routers = APIRouter(
    prefix="/organization",
    tags=["Organization"],
)


@admin_routers.post("/code/")
async def create_code(
    admin: dependency.CompanyPermissionDependency,
    data: schemas.CreateCode,
):
    """Create a verification key to add a user to a company"""
    return await admin_services.RedisServise().create_code(admin, data)


@super_admin_routers.patch(
    "/create_admin/", response_model=schemas.UserResponse
)
async def update_admin_status(
    session: dependency.AsyncSessionDependency,
    current_user: dependency.GetCurrentUserDependency,
    data: schemas.AdminStatus,
):
    """Create admin for company by only superadmin - owner this application"""
    return await admin_services.AdminServices(session).update_admin_status(
        current_user, data
    )


@company_routers.post("/", response_model=schemas.CompanyCreateResponse)
async def create_company(
    session: dependency.AsyncSessionDependency,
    data: schemas.CompanyCreate,
    admin: dependency.AdminPermissionDependency,
):
    """Create company with admin - owner new company"""
    return await admin_services.CompanyServices(session).create_company(
        data, admin
    )


@company_routers.get("/my/", response_model=schemas.CompanyEmployersResponse)
async def get_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
):
    """Get your company - only owner"""
    return await admin_services.CompanyServices(session).get_company(admin)


@company_routers.patch("/my/", response_model=schemas.CompanyCreateResponse)
async def update_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    data: schemas.CompanyCreate,
):
    """Update your company - only owner"""
    return await admin_services.CompanyServices(session).update_company(
        admin, data
    )


@company_routers.delete("/my/")
async def delete_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
):
    """Delete your company - only  owner"""
    return await admin_services.CompanyServices(session).delete_company(admin)


@admin_routers.post("/user/", response_model=schemas.CompanyEmployeers)
async def add_user_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    data: schemas.AddUserOrganization,
):
    """Add another employee in your company - only owner"""
    return await admin_services.AdminServices(session).add_user(data, admin)


@admin_routers.delete("/user/")
async def delete_user_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    data: schemas.AdminStatus,
):
    """Delete employee in your company - only owner"""
    return await admin_services.AdminServices(session).remove_user(data, admin)


@admin_routers.post("/news/", response_model=schemas.CreateNewsResponse)
async def add_news_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    data: schemas.CreateNews,
):
    """Create news for your company - only owner"""
    return await admin_services.AdminServices(session).add_news(data, admin)


@admin_routers.get("/news/", response_model=list[schemas.CreateNewsResponse])
async def get_all_news(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
):
    """Get all news on your company - only owner"""
    return await admin_services.AdminServices(session).get_all_news(admin)


@admin_routers.get(
    "/news/{news_id}", response_model=schemas.CreateNewsResponse
)
async def get_news(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    news_id: int,
):
    """Get some news by id on your company - only owner"""
    return await admin_services.AdminServices(session).get_news(admin, news_id)


@admin_routers.patch(
    "/news/{news_id}", response_model=schemas.CreateNewsResponse
)
async def update_news_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    data: schemas.UpdateNews,
    news_id: int,
):
    """Update news by id on your company - only owner"""
    return await admin_services.AdminServices(session).update_news(
        data, admin, news_id
    )


@admin_routers.delete("/news/{news_id}")
async def delete_news_yours_company(
    session: dependency.AsyncSessionDependency,
    admin: dependency.CompanyPermissionDependency,
    news_id: int,
):
    """Delete news by id on your company - only owner"""
    return await admin_services.AdminServices(session).delete_news(
        admin, news_id
    )
