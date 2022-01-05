import os # utiliser les fonctionnalités dépendantes du système d'exploitation
import argparse # utilisé pour incorporer l'analyse des arguments de ligne de commande
import pandas as pd #manipuler les données
from load_data import read_params
from sklearn.model_selection import train_test_split # Diviser des tableaux ou des matrices en sous-ensembles de train et de test aléatoires

def split_data(df,train_data_path,test_data_path,split_ratio,random_state):
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)
    train.to_csv(train_data_path, sep=",", index=False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index=False, encoding="utf-8")    

def split_and_saved_data(config_path):
    """
    divisez le jeu de données du train (données/brut) et enregistrez-le dans le dossier data/traité
    entrée : chemin de configuration
    sortie : enregistrer les fichiers divisés dans le dossier de sortie
    """
    config = read_params(config_path)
    raw_data_path = config["raw_data_config"]["raw_data_csv"]
    test_data_path = config["processed_data_config"]["test_data_csv"] 
    train_data_path = config["processed_data_config"]["train_data_csv"]
    split_ratio = config["raw_data_config"]["train_test_split_ratio"]
    random_state = config["raw_data_config"]["random_state"]
    raw_df=pd.read_csv(raw_data_path)
    split_data(raw_df,train_data_path,test_data_path,split_ratio,random_state)
    
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)