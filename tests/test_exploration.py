import pandas as pd
import pytest

from app.src.exploration import (
    assign_draft_group,
    resume_performance,
    calcul_scout_score,
    detect_hidden_gems,
    detect_busts
)


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "player_name": ["A", "A", "B", "C"],
        "draft_group": ["Top 15 Picks", "Top 15 Picks", "Mid Picks", "Late Picks"],
        "season": [2020, 2021, 2020, 2020],
        "pts": [10, 20, 15, 25],
        "reb": [5, 6, 7, 8],
        "ast": [2, 3, 4, 5],
        "net_rating": [1, 2, 3, 4],
        "ts_pct": [0.5, 0.6, 0.55, 0.65],
        "gp": [82, 80, 75, 60],
        "oreb_pct": [1, 2, 3, 4],
        "dreb_pct": [2, 3, 4, 5],
        "ast_pct": [1, 2, 3, 4],
        "usg_pct": [10, 20, 15, 25],
        "draft_number": [1, 1, 20, 40]
    })


# ✅ Test assign_draft_group
def test_assign_draft_group():
    assert assign_draft_group(1) == "Top 15 Picks"
    assert assign_draft_group(20) == "Mid Picks"
    assert assign_draft_group(40) == "Late Picks"
    assert assign_draft_group(0) == "Undrafted/Unknown"


# ✅ Test resume_performance
def test_resume_performance(sample_df):
    result = resume_performance(sample_df)

    assert "efficiency" in result.columns
    assert "availability" in result.columns
    assert not result.empty


# ✅ Test calcul_scout_score
def test_calcul_scout_score(sample_df):
    df_perf = resume_performance(sample_df)
    result = calcul_scout_score(df_perf)

    assert "scout_score" in result.columns
    assert result["scout_score"].notnull().all()


# ✅ Test hidden gems
def test_detect_hidden_gems(sample_df):
    df_perf = resume_performance(sample_df)
    df_score = calcul_scout_score(df_perf)

    gems = detect_hidden_gems(df_score)

    assert isinstance(gems, pd.DataFrame)


# ✅ Test busts
def test_detect_busts(sample_df):
    df_perf = resume_performance(sample_df)
    df_score = calcul_scout_score(df_perf)

    busts = detect_busts(df_score)

    assert isinstance(busts, pd.DataFrame)