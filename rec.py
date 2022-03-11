# импортируем ORM для работы с БД
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    ForeignKey,
    func
)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


Base = declarative_base()
PG_ASYNC_CONN_URI = 'postgresql+asyncpg://user:password@localhost/postgres'

# создаем движок
engine = create_async_engine(PG_ASYNC_CONN_URI, echo=False)

Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String, nullable='', default='')
    eye_color = Column(String, nullable='', default='')

    films = Column(String, nullable='', default='')
    gender = Column(String, nullable='', default='')
    hair_color = Column(String, nullable='', default='')

    height = Column(String, nullable='', default='')
    homeworld = Column(String, nullable='', default='')  # planets
    mass = Column(String, nullable='', default='')

    name = Column(String, nullable='', default='')
    skin_color = Column(String, nullable='', default='')
    species = Column(String, nullable='', default='')    # species - cтрока с названиями типов через запятую

    starships = Column(String, nullable='', default='')  # starships - строка с названиями кораблей через запятую
    vehicles = Column(String, nullable='', default='')   # vehicles - строка с названиями транспорта через запятую

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name={self.name!r})'

    def __repr__(self):
        return str(self)


# cоздаем ф-ю, которая сохраняет people в БД
async def save_people_in_db(p_k, people: dict):
    async with Session() as session:
        async with session.begin():
                id = int(p_k)
                birth_year = people['birth_year']
                eye_color = people['eye_color']

                films = people['films']
                gender = people['gender']
                hair_color = people['hair_color']

                height = people['height']
                homeworld = people['homeworld']
                mass = people['mass']

                name = people['name']
                skin_color = people['skin_color']
                species = people['species']

                starships = people['starships']
                vehicles = people['vehicles']

                post = People(id=id, name=name, birth_year=birth_year, eye_color=eye_color, skin_color=skin_color,
                              height=height, gender=gender, mass=mass, hair_color=hair_color,  vehicles = vehicles,
                              homeworld=homeworld, films=films, starships=starships, species=species,
                              )
                session.add(post)




