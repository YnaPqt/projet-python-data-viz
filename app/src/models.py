from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "nbaplayers.db")

engine = create_engine(
    f"sqlite:///{DB_PATH}"
)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    role = Column(String(20), default="user")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)

    player_name = Column(String(100))

    player_height = Column(Float)
    player_weight = Column(Float)

    college = Column(String(100))
    country = Column(String(50))
    draft_year = Column(Integer)
    draft_round = Column(Integer)
    draft_number = Column(Integer)

    season = Column(Integer)
    team_abbreviation = Column(String(10))
    age = Column(Integer)

    gp = Column(Integer)
    pts = Column(Float)
    reb = Column(Float)
    ast = Column(Float)

    net_rating = Column(Float)
    usg_pct = Column(Float)
    ts_pct = Column(Float)
    
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)
    ast_pct = Column(Float)

def init_db():
    Base.metadata.create_all(engine)