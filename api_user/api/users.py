from fastapi.routing import APIRouter


user_router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@user_routers.post("/registration/", response_model=...)
async def create_user(
    session: dependency.AsyncSessionDependency, user_data: ...
):
    """Регистрация пользователей"""
    # verify_path = str(uuid4())
    # redis_client.set(verify_path, user_data.email)
    # user_data.password = security.hash_password(user_data.password)
    # user = await crud.UserCrud(session).create_or_update(
    #     user_data.model_dump(), "create"
    # )
    # await session.commit()
    # await session.refresh(user)
    # send_email.delay(
    #     {
    #         "msg": (
    #             "Чтобы завершить регистрацию, перейдите по ссылке: "
    #             f"{config.BASE_URL}/user/{verify_path}/"
    #         ),
    #         "subject": "Подтверждение регистрации",
    #         "emails": user.email,
    #     }
    # )
    # return user