from pathlib import PurePath

import environ

ENVFILE_PATH = PurePath.joinpath(PurePath(__file__).parent, '.env')
environ.Env.read_env(str(ENVFILE_PATH))

env = environ.Env(
    DEBUG=(bool, False),
)


DEBUG = env('DEBUG', default=False)

__all__ = ['DEBUG']
