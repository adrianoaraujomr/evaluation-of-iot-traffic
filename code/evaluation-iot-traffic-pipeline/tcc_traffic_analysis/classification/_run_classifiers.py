from ._classification_pipeline import ClassificationPipeline
from ..custom_algorithms import CustomAlgorithm
import sys

def run_classifiers(dataset, experimento, tests, scorers, classificadores, feature_selection_methods=[None], holdout=True, grid_search=True, refit="precision_score", persist=False):
    """ dataset - Objeto CustomDataset
        experimento - Identificador do experimento
        tests - Objeto TestingPipeline
        scorers - 
        classificadores - lista  de Nome, Algoritmo, Parametros
        feature_selection_methods - lista de objetos CustomAlgorithms que possui algoritmos de seleção de features
        holdout - flag para terinar coom holdout
        grid_search - flag para terinar usando grid_search
    """
    for classificador in classificadores:
        for feature_selection in feature_selection_methods:
            if grid_search:
                clf = ClassificationPipeline(classificador[0], classificador[1], dataset, classificador[2], scorers, feature_selection=feature_selection, refit=refit)
                clf.train_grid_search()
                if persist:
                    clf.persist_model("/home/adriano/Documentos/evaluation-of-iot-traffic/models")
                tests.set_new_classification_pipeline(clf)
                tests.run_tests()
            if holdout:
                clf = ClassificationPipeline(classificador[0], classificador[1], dataset, classificador[2], scorers, feature_selection=feature_selection, refit=refit)
                clf.train_holdout()
                if persist:
                    clf.persist_model("/home/adriano/Documentos/evaluation-of-iot-traffic/models")
                tests.set_new_classification_pipeline(clf)
                tests.run_tests()
            new_size = len(tests.tests_result['dataset_treino'])                
