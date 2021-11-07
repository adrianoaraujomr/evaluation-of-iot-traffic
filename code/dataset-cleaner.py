#!/usr/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Control Variables ---------------------------------------------------
object_columns = ['Flow ID', 'Src IP', 'Dst IP', 'Timestamp', 'Device Class', 'Label']
path = "/home/adriano/Documentos/evaluation-of-iot-traffic/"

# Functions -----------------------------------------------------------

def remove_device_mac(df):
    try:
        df.drop(['Device MAC'], axis=1, inplace=True)
    except:
        return
    
def remove_unnamed_columns(df):
    will_be_removed = []
    for col in df.columns.values.tolist():
        if 'Unnamed' in col:
            will_be_removed.append(col)
    df.drop(will_be_removed, axis=1, inplace=True)

# Remoção de colunas removidas por questão de generalização
def remove_cols_generalization(df):
    will_be_removed = ["Timestamp", "Flow ID", "Src IP", "Dst IP"]
    for col in will_be_removed:
        try:
            df.drop([col], axis=1, inplace=True)
        except:
            print("not found generalization ", col)
    
# Remção das colunas que apresentavam apenas um valor para todas linhas no dataset completo
def remove_cols_all_same_value(df):
    will_be_removed = ['Fwd URG Flags', 'URG Flag Count', 'CWE Flag Count', 
                       'ECE Flag Count', 'Fwd Bytes/Bulk Avg', 'Fwd Packet/Bulk Avg', 
                       'Fwd Bulk Rate Avg', 'Bwd Bytes/Bulk Avg', 'Bwd Packet/Bulk Avg', 
                       'Bwd Bulk Rate Avg']
    try:
        df.drop(will_be_removed, axis=1, inplace=True)
    except:
        print("not found cols same value")
        
def remove_trouble_cols(df):
    will_be_removed = ["Subflow Fwd Packets", "Subflow Bwd Packets"]
    try:
        df.drop(will_be_removed, axis=1, inplace=True)
    except:
        print("not found troublesome cols")
    
# Remove se existir linhas que possuem o valor 'No Label' nas colunas 'Bwd Header Len' e 'Bwd PSH Flags'
def remove_no_label(df):
    head  = df["Bwd Header Length"]
    flag  = df["Bwd PSH Flags"]
    indxs = []
    
    indxs += flag[flag == 'No Label'].index.values.tolist() #This line dont make sense
    indxs += head[head == 'No Label'].index.values.tolist()

    df.drop(indxs, axis=0, inplace=True)
    df = df.reset_index()
    df.drop(["index"], axis=1, inplace=True)
    
    convert_cols_no_label(df)
    
# Converte as colunas 'Bwd Header Len' e 'Bwd PSH Flags' para seu tipo verdadeiro
def convert_cols_no_label(df):
    x = []

    h_aux_1 = df["Bwd Header Length"]
    h_aux_2 = df["Bwd PSH Flags"]

    x += h_aux_1[h_aux_1.isna()].index.values.tolist()
    x += h_aux_2[h_aux_2.isna()].index.values.tolist()

    df.drop(x, axis=0, inplace=True)
    df = df.reset_index()
    df.drop(["index"], axis=1, inplace=True)
    
    cols = ["Bwd Header Length", "Bwd PSH Flags"]
    for col in cols:
        df[col] = df[col].astype('float64')
        
# -------------------------------------------------------------------
def find_object_columns(df):
    aux = df.dtypes
    obj_types = aux[aux == 'object'].index.values.tolist()
    result = [x for x in obj_types if x not in object_columns]
    return result
                
def is_infinity(value):
    if 'inf' in str(value).lower():
        return True
    return False

def find_strings_or_infinity(df):
    possible_cols = find_object_columns(df)
    to_drop = []
    for column in possible_cols:
        aux = df[column]
        to_drop += df[aux.apply(lambda x: is_infinity(x) )].index.values.tolist()
    
    return (list(set(to_drop)), possible_cols)
# --------------------------------------------------------------------

def drop_columns(df):
    remove_unnamed_columns(df)
    remove_no_label(df)
    remove_cols_generalization(df)
    remove_cols_all_same_value(df)
    remove_trouble_cols(df)
    return df

def drop_lines(df):
    df = df.dropna()
    lines, cols = find_strings_or_infinity(df)
    df = df.drop(lines)
    return df

# Main ---------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("database", help="caminho + nome do arquivo que contem a base de dados")
    parser.add_argument("-det", help="flag usada quando se quer fazer apenas o passo de detectar valores faltantes, infinitos, strings", action='store_true', default=False)
    
    args = parser.parse_args()
    file_name = args.database
    df = pd.read_csv(path + file_name)
    if args.det:
        lines, cols = find_strings_or_infinity(df)
        if(len(lines) > 0):
            print("found strings or infinity in columns: ", cols)
            print(lines)
            print(df.loc[lines, cols])
    else:
        df = drop_columns(df)
        df = drop_lines(df)
        remove_device_mac(df)
        df.to_csv(path + file_name.replace(".csv","cleaned.csv"), index=False)
