#!/usr/bin/python3

import sys
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import argparse
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Global Variables ---------------------------------------------------

classes   = ["Controller/HUBS", "Cameras", "Energy Managment", "Health Monitor", "Appliences"]
iot_df_file = '../datasets/original/benignos/cleaned/iotPerDeviceCleaned.csv'
full_df_file = '../datasets/original/benignos/cleaned/dataSetCleaned.csv'
anom_df_file = '../datasets/original/anomalias/dataset-cleaned.csv'

# Functions ----------------------------------------------------------

def read_benign_dataset():
    return pd.read_csv(full_df_file)

def read_anomaly_dataset():
    return pd.read_csv(anom_df_file)

def read_iot_dataset():
    return pd.read_csv(iot_df_file)

def merge_dataset(dataset, indices_list):
    result = []
    for indices in indices_list:
        result.append(dataset.iloc[indices])
    return pd.concat(result)

def calculate_ds_lines(iot_percent, nrm_percent, mbl_percent, total_size, anom_percent=0):
    if anom_percent <= 0:
        iot_lines = int(iot_percent * total_size)
        nrm_lines = int(nrm_percent * (1 - iot_percent) * total_size)
        mbl_lines = int(mbl_percent * (1 - iot_percent) * total_size)    
        return [iot_lines, nrm_lines, mbl_lines]
    else:
        anom_lines = int(anom_percent * total_size)
        iot_lines = int((1 - anom_percent) * iot_percent * total_size)
        nrm_lines = int((1 - anom_percent) * nrm_percent * (1 - iot_percent) * total_size)
        mbl_lines = int((1 - anom_percent) * mbl_percent * (1 - iot_percent) * total_size)    
        return [iot_lines, nrm_lines, mbl_lines, anom_lines]

def generate_dataset_1(dataset, iot_lines, nrm_lines, mbl_lines):
    sel_indices_iot = np.random.choice(dataset[dataset['Device Class'] == 'Iot'].index, iot_lines, replace=False)
    sel_indices_mob = np.random.choice(dataset[dataset['Device Class'] == 'Mobile'].index, nrm_lines, replace=False)
    sel_indices_tor = np.random.choice(dataset[dataset['Device Class'] == 'Non Tor'].index, mbl_lines, replace=False)
    
    df = merge_dataset(dataset, [sel_indices_iot, sel_indices_mob, sel_indices_tor])
    return df
    
def generate_experimento_1(root_path, file_name, dataset, iot_percent, nrm_percent, mbl_percent, total_size):
    iot_lines, nrm_lines, mbl_lines = calculate_ds_lines(iot_percent, nrm_percent, mbl_percent, total_size)
    df = generate_dataset_1(dataset, iot_lines, nrm_lines, mbl_lines)
    df.to_csv(root_path + file_name.replace(".csv", "-train.csv"), index=False)
    df = generate_dataset_1(dataset, iot_lines, nrm_lines, mbl_lines)
    df.to_csv(root_path + file_name.replace(".csv", "-test.csv"), index=False)

def select_random_rows_device_class(df, rows, sel_classes):
    new_df_idxs = np.array([])

    for device in sel_classes:
        aux_df = np.random.choice(df[df['Device Class'] == device].index, rows, replace=False)
        new_df_idxs = np.concatenate([new_df_idxs, aux_df])
    aux = df.iloc[new_df_idxs]
    print(aux['Device Class'].value_counts())
    return new_df_idxs    
    
def generate_experimento_2(root_path, file_name, dataset, iot_percent, nrm_percent, mbl_percent, total_size, max_num_classes):
    iot_lines, nrm_lines, mbl_lines = calculate_ds_lines(iot_percent, nrm_percent, mbl_percent, total_size)
    
    # Criar all iot
    num_classes = len(classes)
    rows = int(iot_lines/num_classes)
    sel_classes  = classes

    sel_indices_iot = select_random_rows_device_class(dataset, rows, sel_classes)
    sel_indices_mob = np.random.choice(dataset[dataset['Device Class'] == 'Mobile'].index, mbl_lines, replace=False)
    sel_indices_tor = np.random.choice(dataset[dataset['Device Class'] == 'Non Tor'].index, nrm_lines, replace=False)
        
    df = merge_dataset(dataset, [sel_indices_iot, sel_indices_mob, sel_indices_tor])
    df = df.sort_values(by="Device Class")
    df.to_csv(root_path + "all_iot_" + file_name.replace(".csv", "-train.csv"), index=False)

    # Criar por classe
    for classe in classes:
        aux = classes[:]
        aux.remove(classe)
        aux = np.array(aux)
        num_classes = random.randint(1, max_num_classes)
        rows = int(iot_lines/num_classes)
        sel_classes  = np.random.choice(aux, num_classes, replace=False)
        
        sel_indices_iot = select_random_rows_device_class(dataset, rows, sel_classes)
        sel_indices_mob = np.random.choice(dataset[dataset['Device Class'] == 'Mobile'].index, mbl_lines, replace=False)
        sel_indices_tor = np.random.choice(dataset[dataset['Device Class'] == 'Non Tor'].index, nrm_lines, replace=False)
        
        df = merge_dataset(dataset, [sel_indices_iot, sel_indices_mob, sel_indices_tor])
        df = df.sort_values(by="Device Class")
        df.to_csv(root_path + classe.lower().replace(" ", "-").replace("/","-") + "_" + file_name.replace(".csv", "-train.csv"), index=False)
        
        sel_indices_iot = np.random.choice(dataset[dataset['Device Class'] == classe].index, iot_lines, replace=False)
        sel_indices_mob = np.random.choice(dataset[dataset['Device Class'] == 'Mobile'].index, mbl_lines, replace=False)
        sel_indices_tor = np.random.choice(dataset[dataset['Device Class'] == 'Non Tor'].index, nrm_lines, replace=False)
        
        df = merge_dataset(dataset, [sel_indices_iot, sel_indices_mob, sel_indices_tor])
        df = df.sort_values(by="Device Class")
        df.to_csv(root_path + classe.lower().replace(" ", "-").replace("/","-") + "_" + file_name.replace(".csv", "-test.csv"), index=False)
        
def generate_dataset_3(dataset_bng, dataset_anom, iot_lines, nrm_lines, mbl_lines, anom_lines):
    sel_indices_iot = np.random.choice(dataset_bng[dataset_bng['Device Class'] == 'Iot'].index, iot_lines, replace=False)
    sel_indices_mob = np.random.choice(dataset_bng[dataset_bng['Device Class'] == 'Mobile'].index, nrm_lines, replace=False)
    sel_indices_tor = np.random.choice(dataset_bng[dataset_bng['Device Class'] == 'Non Tor'].index, mbl_lines, replace=False)
    sel_indices_anom = np.random.choice(dataset_anom.index, anom_lines, replace=False)
    
    df_bng = merge_dataset(dataset_bng, [sel_indices_iot, sel_indices_mob, sel_indices_tor])    
    df_anm = merge_dataset(dataset_anom, [sel_indices_anom])
    
    df = pd.concat([df_bng, df_anm])
    df = df.sort_values(by="Device Class")
    return df
        
def generate_experimento_3(root_path, file_name, dataset_bng, dataset_anom, iot_percent, nrm_percent, mbl_percent, anom_percent, total_size):
    iot_lines, nrm_lines, mbl_lines, anom_lines = calculate_ds_lines(iot_percent, nrm_percent, mbl_percent, total_size, anom_percent=anom_percent)
    df = generate_dataset_3(dataset_bng, dataset_anom, iot_lines, nrm_lines, mbl_lines, anom_lines)
    df.to_csv(root_path + "anomaly_" + file_name.replace(".csv", "-train.csv"), index=False)
    df = generate_dataset_3(dataset_bng, dataset_anom, iot_lines, nrm_lines, mbl_lines, anom_lines)
    df.to_csv(root_path + "anomaly_" + file_name.replace(".csv", "-test.csv"), index=False)
        
# Main ---------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="caminho diretorio para salvar")
    parser.add_argument("dssize", help="numero total de linhas que o dataset deve ter", type=int)
    parser.add_argument("id", help="identificador para o dataset")
    parser.add_argument("-nrodatasets", help="numero de datasets a serem criados", default=5, type=int)
    parser.add_argument("-exp1", help="flag para identificar como experimento 1", action='store_true', default=False)
    parser.add_argument("-exp2", help="flag para identificar como experimento 2", action='store_true', default=False)
    parser.add_argument("-exp3", help="flag para identificar como experimento 3", action='store_true', default=False)
    parser.add_argument("-iot", help="porcentagem de trafego iot", default=0.5, type=float)
    parser.add_argument("-nrm", help="porcentagem de trafego normal", default=0.5, type=float)
    parser.add_argument("-mbl", help="porcentagem de trafego mobile", default=0.5, type=float)
    parser.add_argument("-anom", help="porcentagem de anomalias", default=0.5, type=float)
    parser.add_argument("-maxclasses", help="numero de classes de iot no dataset", default=4, type=int)
    
    args = parser.parse_args()

    if args.exp1:
        dataset = read_benign_dataset()
        #Checar se o nome esta correto ordem mobile normal
        for i in range(args.nrodatasets):
            file_name = '{:02.0f}'.format(args.iot * 10) + "_" + '{:02.0f}'.format(args.mbl * 10) + "_" + '{:02.0f}'.format(args.nrm * 10) + "-" + args.id + str(i) + ".csv"
            generate_experimento_1(args.directory + "/", file_name, dataset, args.iot, args.mbl, args.nrm, args.dssize)
    if args.exp2:
        dataset_iot = read_iot_dataset().drop(['Device MAC'], axis=1)
        dataset_bng = read_benign_dataset()
        dataset = pd.concat([dataset_iot, dataset_bng], sort=True)
        dataset = dataset.reset_index(drop=True)
        #print(dataset['Device Class'].value_counts())
        for i in range(args.nrodatasets):
            file_name = '{:02.0f}'.format(args.iot * 10) + "_" + '{:02.0f}'.format(args.mbl * 10) + "_" + '{:02.0f}'.format(args.nrm * 10) + "-" + args.id + str(i) + ".csv"
            generate_experimento_2(args.directory + "/", file_name, dataset, args.iot, args.mbl, args.nrm, args.dssize, args.maxclasses)
    if args.exp3:
        dataset_bng = read_benign_dataset()
        dataset_anm = read_anomaly_dataset()
        for i in range(args.nrodatasets):
            file_name = '{:02.0f}'.format(args.iot * 10) + "_" + '{:02.0f}'.format(args.mbl * 10) + "_" + '{:02.0f}'.format(args.nrm * 10) + "-" + args.id + str(i) + ".csv"
            generate_experimento_3(args.directory + "/", file_name, dataset_bng, dataset_anm, args.iot, args.mbl, args.nrm, args.anom, args.dssize)
