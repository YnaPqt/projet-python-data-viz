from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine(
    "sqlite:///../data/nbaplayers.db"
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

    id = Column(Integer, primary_key=True, autoincrement=True)
    # identité
    player_name = Column(String(100))
    team_abbreviation = Column(String(10))
    age = Column(Float)
    season = Column(String(10))
    # physique
    player_height = Column(Float)
    player_weight = Column(Float)
    # background
    college = Column(String(100))
    country = Column(String(50))
    draft_year = Column(String(20))
    draft_round = Column(String(10))
    draft_number = Column(String(10))

    stats = relationship("PlayerStat", back_populates="player")



class PlayerStat(Base):
    __tablename__ = "players_stats"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"))

    # performance
    gp = Column(Integer)
    pts = Column(Float)
    reb = Column(Float)
    ast = Column(Float)

    # advanced stats
    net_rating = Column(Float)
    usg_pct = Column(Float)
    ts_pct = Column(Float)

    # rebounding
    oreb_pct = Column(Float)
    dreb_pct = Column(Float)

    # playmaking
    ast_pct = Column(Float)

    player = relationship("Player", back_populates="stats")

def init_db():
    Base.metadata.create_all(engine)