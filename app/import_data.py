from data_processing import load_csv, clean_data
from models import engine, init_db

def save_db(filepath: str):
    df = load_csv(filepath)