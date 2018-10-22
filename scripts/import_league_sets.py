import pandas as pd
import os

LEAGUE_PATH = "datasets/League"

def load_summer_data(league_path=LEAGUE_PATH):
    csv_path = os.path.join(league_path, "2018_Summer_League.csv")
    return pd.read_csv(csv_path)

def load_spring_data(league_path=LEAGUE_PATH):
    csv_path = os.path.join(league_path, "2018_Spring_League.csv")
    return pd.read_csv(csv_path)

def load_2018_worlds_data(league_path=LEAGUE_PATH):
    csv_path = os.path.join(league_path, "2018_worlds.csv")
    return pd.read_csv(csv_path)
