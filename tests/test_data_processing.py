import pandas as pd
import pytest
from src.data_processing import clean_data


def create_sample_df():
    return pd.DataFrame({
        "Unnamed: 0": [1, 2, 2],
        "college": ["Duke", None, None],
        "draft_number": ["1", "Undrafted", "Undrafted"],
        "draft_year": ["2020", "Undrafted", "Undrafted"],
        "draft_round": ["1", "Undrafted", "Undrafted"],
        "season": ["2020-21", "2019-20", "2019-20"]
    })


def test_clean_data_removes_unnamed_column():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert "Unnamed: 0" not in cleaned.columns


def test_clean_data_removes_duplicates():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert len(cleaned) < len(df)


def test_clean_data_fills_missing_college():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert "Unknown" in cleaned["college"].values


def test_clean_data_converts_undrafted_to_zero():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert (cleaned["draft_number"] == 0).any()
    assert (cleaned["draft_round"] == 0).any()
    assert (cleaned["draft_year"] == 0).any()


def test_clean_data_types_are_int():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert cleaned["draft_number"].dtype == int
    assert cleaned["draft_round"].dtype == int
    assert cleaned["draft_year"].dtype == int


def test_clean_data_extracts_season_year():
    df = create_sample_df()
    cleaned = clean_data(df.copy())

    assert cleaned["season"].iloc[0] == 2020