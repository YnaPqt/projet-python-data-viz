import pytest
from sqlalchemy import inspect
from src.models import Base, engine, Session, User, Player, init_db


@pytest.fixture(scope="module")
def setup_db():
    # Créer les tables
    init_db()
    yield
    # Nettoyage après tests
    Base.metadata.drop_all(engine)


def test_tables_exist(setup_db):
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    assert "users" in tables
    assert "players" in tables


def test_create_user(setup_db):
    session = Session()

    user = User(
        username="test_user",
        password_hash="hashed_pwd"
    )

    session.add(user)
    session.commit()

    result = session.query(User).filter_by(username="test_user").first()

    assert result is not None
    assert result.username == "test_user"


def test_unique_username_constraint(setup_db):
    session = Session()

    user1 = User(username="unique_user", password_hash="pwd1")
    user2 = User(username="unique_user", password_hash="pwd2")

    session.add(user1)
    session.commit()

    session.add(user2)

    with pytest.raises(Exception):
        session.commit()

    session.rollback()


def test_insert_player(setup_db):
    session = Session()

    player = Player(
        id=1,
        player_name="Test Player",
        player_height=2.0,
        player_weight=100,
        college="Test College",
        country="USA",
        draft_year=2020,
        draft_round=1,
        draft_number=1,
        season=2020,
        team_abbreviation="LAL",
        age=25,
        gp=10,
        pts=20.5,
        reb=5.0,
        ast=3.0
    )

    session.add(player)
    session.commit()

    result = session.query(Player).filter_by(id=1).first()

    assert result is not None
    assert result.player_name == "Test Player"