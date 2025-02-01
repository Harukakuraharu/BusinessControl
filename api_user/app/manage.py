#! /usr/bin/env python
import json

import click
import sqlalchemy as sa
<<<<<<< HEAD
<<<<<<< HEAD
from core.settings import config
from database import models
from pydantic import ValidationError
from schemas import schemas
from sqlalchemy.orm import Session
from tests_config.utils import hash_password
=======
=======
from core.settings import config
>>>>>>> e7f03f9 (Added docs)
from database import models
from pydantic import ValidationError
from schemas import schemas
<<<<<<< HEAD

from core.settings import config
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
from sqlalchemy.orm import Session
from tests_config.utils import hash_password
>>>>>>> e7f03f9 (Added docs)


@click.group("db")
def db():
    pass


@db.command
@click.option("-e", "--email", prompt=True, help="Admin email")
@click.option("-f", "--first_name", prompt=True, help="Admin first name")
@click.option("-l", "--last_name", prompt=True, help="Admin last name")
@click.option(
    "-p", "--password", prompt=True, hide_input=True, help="Admin password"
)
def create_admin(email, first_name, last_name, password):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e7f03f9 (Added docs)
    data = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password,
    }
<<<<<<< HEAD
=======
    data = {"email": email, "first_name": first_name, "last_name": last_name, "password": password}
>>>>>>> 3f2822f (Complete servis with admin and company)
=======
>>>>>>> e7f03f9 (Added docs)
    try:
        schemas.UserCreate.model_validate_json(json.dumps(data))
    except ValidationError as err:
        for e in err.errors():
            click.echo(f"{e['loc']}: {e['msg']}")
        return
    with Session(sa.create_engine(config.dsn)) as session:
        data["is_super_admin"] = True
        data["password"] = hash_password(data["password"])
        session.scalar(
            sa.insert(models.User).values(**data).returning(models.User)
        )
        session.commit()


if __name__ == "__main__":
    db()
