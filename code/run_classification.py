#!/usr/bin/python

from tcc_traffic_analysis.testing import TestingPipeline
from tcc_traffic_analysis.custom_algorithms import CustomAlgorithm
from tcc_traffic_analysis.custom_algorithms import ManualFeatureSelection
from tcc_traffic_analysis.classification import ClassificationPipeline
from tcc_traffic_analysis.datasets import CustomDataSet

from tcc_traffic_analysis.classification import run_classifiers
import os
import json
import random
from datetime import date

from sklearn.metrics import classification_report
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from xgboost import XGBClassifier

import pandas as pd


def create_classifiers():
    classificadores = []
    clf = ("Gaussian Naive Bayes", GaussianNB(), {})
    classificadores.append(clf)
    clf = ("Knn", KNeighborsClassifier(), {})
    classificadores.append(clf)
    clf = ('MLP', MLPClassifier(), {})
    classificadores.append(clf)
    clf = ("XGBoost", XGBClassifier(), {})
    classificadores.append(clf)
    clf = ("Linear Discriminant Analysis", LinearDiscriminantAnalysis(), {})
    classificadores.append(clf)
    clf = ("Quadratic Discriminant Analysis ", QuadraticDiscriminantAnalysis(), {})
    classificadores.append(clf)
    clf = ("Decision Trees", DecisionTreeClassifier(), {})
    classificadores.append(clf)
    clf = ("Random Forests", RandomForestClassifier(), {})
    classificadores.append(clf)
    clf = ("Gradient Boosting", GradientBoostingClassifier(), {})
    classificadores.append(clf)
    clf = ("Ada Boosting", AdaBoostClassifier(), {})
    classificadores.append(clf)
    return classificadores

def create_scorers():
    scorers = {'accuracy_score': make_scorer(accuracy_score),
               'precision_score': make_scorer(precision_score, average='micro'),
               'f1_score': make_scorer(f1_score, average='micro'),
               'recall_score': make_scorer(recall_score, average='micro')}
    return scorers

def generate_test_dataset_list(dataset_path, dataset_name_std, dataset_id, ext=".csv", num_datasets=5, path_in_name=False):
    tests = []
    for i in range(0, num_datasets):
        if path_in_name:
            tests.append(dataset_path + dataset_name_std + str(dataset_id + i) + ext)
        else:
            tests.append(dataset_name_std + str(dataset_id + i) + ext)
    return tests

def generate_manual_feature_selection_method():
    metrics           = ["Mutual information", "Importance", "Abs Correlation"]
    n_features_keeps  = [10, 20, 30, 40]
    result_control_id = 1
    jump_control      = 5
    result = []
    for n_features_keep in n_features_keeps:
        for metric in metrics:
            if result_control_id > jump_control:
                fs = CustomAlgorithm(metric + " " + str(n_features_keep), ManualFeatureSelection(metric, n_features_keep))
                result.append(fs)
                result_control_id += 1
            else:
                result_control_id += 1
    return result
                
def generate_feature_selection_algorithms():
    fs_1 = CustomAlgorithm("Tree", SelectFromModel(ExtraTreesClassifier()))
    fs_2 = CustomAlgorithm("PCA" , PCA())
    manual = generate_manual_feature_selection_method()
    return [fs_1, fs_2] + manual

def device_class_tor_non_tor_transform(dataset, column_name, rows=None):
    # Iot 1, Non Iot 0
    if rows is not None:
        return dataset[column_name].apply(lambda x: 0 if x in ["Non Tor", "Mobile"] else 1).iloc[rows]
    else:
        return dataset[column_name].apply(lambda x: 0 if x in ["Non Tor", "Mobile"] else 1) 
    
def device_class_tor_non_tor_iot_class_transform(dataset, column_name, rows=None):
    # Iot 1, Non Iot 0
    if rows is not None:
        return dataset[column_name].apply(lambda x: 0 if x in ["Non Tor", "Mobile"] else 1).iloc[rows]
    else:
        return dataset[column_name].apply(lambda x: 0 if x in ["Non Tor", "Mobile"] else 1) 
    
def device_class_anom_transform(dataset, column_name, rows=None):
    # Benigno 0, Anomalia 1
    if rows is not None:
        return dataset[column_name].apply(lambda x: 0 if "Anomaly" not in x else 1).iloc[rows]
    else:
        return dataset[column_name].apply(lambda x: 0 if "Anomaly" not in x else 1) 


def run_experimento_1():
    datasets = [("./datasets/experimento-1/iot-mobile-nontor/", "05_05_05-"),
                  ("./datasets/experimento-1/iot-mobile/", "05_10_00-"),
                  ("./datasets/experimento-1/iot-nontor/", "05_00_10-")]
    dataset_ids = [90]
    num_datasets = 5
    test_size = 0.3
    today = date.today().strftime('%d-%m-%Y')
    experimento = '1'
    final_ds = pd.DataFrame()

    for dataset_id in dataset_ids:
        files_to_test = []
        for train_dataset in datasets:
            dataset_path = train_dataset[0]
            dataset_name_std = train_dataset[1]
            files_to_test += generate_test_dataset_list(dataset_path, dataset_name_std, dataset_id, path_in_name=True, ext="-testcleaned.csv")
        for train_dataset in datasets:
            dataset_path = train_dataset[0]
            dataset_name_std = train_dataset[1]
            print("Doing", dataset_path + dataset_name_std)
            for i in range(0, num_datasets):
                print("\t", i)
                new_dataset_id = dataset_id + i
                dataset_file = dataset_path + dataset_name_std + str(new_dataset_id) + "-traincleaned.csv"

                feature_selection_methods = generate_feature_selection_algorithms()
                classifiers = create_classifiers()
                scorers = create_scorers()

                tests = TestingPipeline(None, files_to_test, y_function=device_class_tor_non_tor_transform, name_in_path=True)
                df = CustomDataSet(dataset_name_std + str(new_dataset_id) + "-traincleaned.csv", dataset_file, test_size=test_size, y_function=device_class_tor_non_tor_transform)
                print("\t", dataset_file)
                run_classifiers(df, experimento, tests, scorers, classifiers, feature_selection_methods)
            
                final_ds = pd.concat([final_ds, tests.return_dataframe()])
            final_ds.to_csv("./resultados/experimento-" + experimento + "/resultado_" + "experimento_" + experimento + "-" + str(dataset_id) + "-" + today + ".csv")    


def run_experimento_2(case_base=False):
    train_datasets = [("./datasets/experimento-2/all_iot/", "all_iot_05_05_05-")]
    test_datasets = [
                   ("./datasets/experimento-2/appliences/", "appliences_05_05_05-"),
                   ("./datasets/experimento-2/cameras/", "cameras_05_05_05-"),
                   ("./datasets/experimento-2/controller_hubs/", "controller-hubs_05_05_05-"),
                  ("./datasets/experimento-2/energy_managment/", "energy-managment_05_05_05-"),
                   ("./datasets/experimento-2/health_monitor/", "health-monitor_05_05_05-")
    ]
    if not case_base:
        train_datasets = test_datasets

    dataset_ids = [100]
    num_datasets = 5
    test_size = 0.3
    today = date.today().strftime('%d-%m-%Y')
    experimento = '2'
    final_ds = pd.DataFrame()

    print("Experimento 2")
    print(train_datasets)
    for dataset_id in dataset_ids:
        files_to_test = []
        for train_dataset in train_datasets:
            if not case_base:
                dataset_test_path = train_dataset[0]
                dataset_test_name_std = train_dataset[1]
                files_to_test += generate_test_dataset_list(dataset_test_path, dataset_test_name_std, dataset_id, path_in_name=True, ext="-test.csv") 
            else:
                for test_dataset in test_datasets:
                    dataset_test_path = test_dataset[0]
                    dataset_test_name_std = test_dataset[1]
                    files_to_test += generate_test_dataset_list(dataset_test_path, dataset_test_name_std, dataset_id, path_in_name=True, ext="-test.csv")
            dataset_path = train_dataset[0]
            dataset_name_std = train_dataset[1]
            print("Doing", dataset_path + dataset_name_std)
            for i in range(0, num_datasets):
                print("\t", i)
                new_dataset_id = dataset_id + i
                dataset_file = dataset_path + dataset_name_std + str(new_dataset_id) + "-train.csv"
            
                feature_selection_methods = generate_feature_selection_algorithms()
                classifiers = create_classifiers()
                scorers = create_scorers()
            
                tests = TestingPipeline(dataset_path, files_to_test, y_function=device_class_tor_non_tor_transform, name_in_path=True)
                df = CustomDataSet(dataset_name_std + str(new_dataset_id) + "-trains.csv", dataset_file, test_size=test_size, y_function=device_class_tor_non_tor_transform)
                run_classifiers(df, experimento, tests, scorers, classifiers, feature_selection_methods)
            
                final_ds = pd.concat([final_ds, tests.return_dataframe()])
            if case_base:
                final_ds.to_csv("./resultados/experimento-" + experimento + "/resultado_" + "experimento_" + experimento + "_base_hip-" + str(dataset_id) + "-" + today + ".csv")
            else:
                final_ds.to_csv("./resultados/experimento-" + experimento + "/resultado_" + "experimento_" + experimento + "-" + str(dataset_id) + "-" + today + ".csv")


if __name__ == "__main__":
    run_experimento_1()
    run_experimento_2()
    run_experimento_2(True)