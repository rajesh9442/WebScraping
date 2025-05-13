# Data preprocessing code placeholder
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np

def clean_text(text):
    return " ".join(BeautifulSoup(text, "html.parser").get_text().lower().split())

def preprocess(df):
    df["description"] = df["description"].apply(clean_text)
    df["posted_date"] = pd.to_datetime(df["posted_date"], errors='coerce')
    df["days_since_posted"] = (datetime.utcnow() - df["posted_date"]).dt.days
    df["salary_numeric"] = df["salary"].str.extract(r"(\d{2,3}k)").replace("k", "", regex=True).astype(float)
    df["location"].fillna("Remote", inplace=True)
    df.drop_duplicates(subset=["id"], inplace=True)
    return df
