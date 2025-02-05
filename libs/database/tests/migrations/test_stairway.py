"""
Test can find forgotten downgrade methods, undeleted data types in downgrade
methods, typos and many other errors.

Does not require any maintenance - you just add it once to check 80% of typos
and mistakes in migrations forever.
"""

import pytest
from alembic.command import downgrade, upgrade
from alembic.config import Config
from alembic.script import Script, ScriptDirectory

<<<<<<< HEAD
<<<<<<< HEAD
from database.core.settings import config
from database.tests.utils import make_alembic_config
=======
from core.settings import config
from tests.utils import make_alembic_config
>>>>>>> a0a9e11 (Fix folders)
=======
from database.core.settings import config
from database.tests.utils import make_alembic_config
>>>>>>> 09b7086 (Add user routers)


def get_revisions():
    # Create Alembic configuration object
    # (we don't need database for getting revisions list)
    config.DB_HOST = "localhost"
<<<<<<< HEAD
<<<<<<< HEAD
    alembic_config = make_alembic_config(config.dsn, "database")
=======
    alembic_config = make_alembic_config(config.dsn)
>>>>>>> a0a9e11 (Fix folders)
=======
    alembic_config = make_alembic_config(config.dsn, "database")
>>>>>>> 0f0357a (Fix migrations and tests)
    # Get directory object with Alembic migrations
    revisions_dir = ScriptDirectory.from_config(alembic_config)

    # Get & sort migrations, from first to last
    revisions = list(revisions_dir.walk_revisions("base", "heads"))
    revisions.reverse()
    return revisions


@pytest.mark.parametrize("revision", get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script):
    upgrade(alembic_config, revision.revision)

    # We need -1 for downgrading first migration (its down_revision is None)
    downgrade(alembic_config, revision.down_revision or "-1")  # type: ignore
    upgrade(alembic_config, revision.revision)
