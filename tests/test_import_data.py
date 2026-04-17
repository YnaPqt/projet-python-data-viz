import pandas as pd
from unittest.mock import patch
from src.import_data import save_to_db


def test_save_to_db_calls_to_sql():
    df = pd.DataFrame({
        "name": ["Player1", "Player2"],
        "points": [10, 20]
    })

    with patch("pandas.DataFrame.to_sql") as mock_to_sql:
        save_to_db(df)

        mock_to_sql.assert_called_once()


def test_save_to_db_empty_dataframe():
    df = pd.DataFrame()

    with patch("pandas.DataFrame.to_sql") as mock_to_sql:
        save_to_db(df)

        mock_to_sql.assert_not_called()