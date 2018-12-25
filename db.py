from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from models import Base


def build_engine_url():
    url = [
        settings.DATABASE_ENGINE,
        '://'
    ]

    if settings.DATABASE_USER:
        url.append(settings.DATABASE_USER)

        if settings.DATABASE_PASSWORD:
            url.append(':')
            url.append(settings.DATABASE_PASSWORD)

        if settings.DATABASE_HOST:
            url.append('@')

    if settings.DATABASE_HOST:
        url.append(settings.DATABASE_HOST)

        if settings.DATABASE_PORT:
            url.append(':')
            url.append(str(settings.DATABASE_PORT))

        url.append('/')

    url.append(settings.DATABASE_NAME)

    return ''.join(url)

engine_url = build_engine_url()
engine = create_engine(engine_url)
Session = sessionmaker(bind=engine)

print('Connected to database engine "{}" with name "{}"'.format(settings.DATABASE_ENGINE, settings.DATABASE_NAME))

Base.metadata.create_all(engine)