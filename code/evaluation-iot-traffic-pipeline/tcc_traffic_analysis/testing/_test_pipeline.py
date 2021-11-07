import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

from ..datasets import CustomDataSet

class TestingPipeline:
    def __init__(self, datasets_path, test_datasets, scorers=None, classification_pipeline=None, 
                 x_function=None, y_function=None, debug=False, name_in_path=False):
        self.test_path = datasets_path
        self.test_datasets = test_datasets
        self.name_in_path = name_in_path
        self.classification_pipeline = classification_pipeline
        self.x_transform_function = x_function
        self.y_transform_function = y_function
        self.scorers = scorers
        self.debug = debug
        self.new_results_dictionary()
    
    def new_results_dictionary(self):
        self.tests_result = {
            'algoritmo'      : [],
            'train_method'   : [],
            'normalizacao'   : [],
            'selecao_feat'   : [],
            'dataset_treino' : [],
            'dataset_test'   : [],
            'acuracia'       : [],
            'precisao'       : [],
            'recall'         : [],
            'f1'             : []
        }
        if self.scorers is not None:
            for scorer in self.scorers.keys():
                self.tests_result[scorer] = []
        
    def save_test_result(self, test, accuracy, recall, precision, f1):
        self.tests_result['algoritmo'].append(self.classification_pipeline.algorithm)
        self.tests_result['train_method'].append(self.classification_pipeline.train_method)
        self.tests_result['normalizacao'].append(self.classification_pipeline.normalization.name)
        self.tests_result['selecao_feat'].append(self.classification_pipeline.feature_selection.name)
        self.tests_result['dataset_treino'].append(self.classification_pipeline.dataset.name)
        self.tests_result['dataset_test'].append(test)
        self.tests_result['acuracia'].append(accuracy)
        self.tests_result['precisao'].append(precision)
        self.tests_result['recall'].append(recall)
        self.tests_result['f1'].append(f1)
    
    def persist_results(self, directory, file_name):    
        aux_df = pd.DataFrame(self.tests_result)
        aux_df.to_csv(directory + file_name)
    
    def return_dataframe(self):
        return pd.DataFrame(self.tests_result)
    
    def set_new_classification_pipeline(self, clf):
        self.classification_pipeline = clf

    def get_scores(self, y, predictions):
        if self.debug:
            print("y", len(y))
            print("predictions", len(predictions))
        acc_test = accuracy_score(y, predictions)
        recall_test = recall_score(y, predictions, average='binary', zero_division=0)
        precision_test = precision_score(y, predictions, average='binary')
        f1_test = f1_score(y, predictions, average='binary')
        return [acc_test, recall_test, precision_test, f1_test]

    def run_scorers(self, base_dataset):
        for scorer in self.scorers.keys():
            self.tests_result[scorer].append(self.scorers[scorer](self.classification_pipeline.estimator, base_dataset.x(), base_dataset.y()))

    def new_dataset(self, test_file, test_file_path):
        if   self.x_transform_function is not None and self.y_transform_function is not None:
            base_dataset = CustomDataSet(test_file, test_file_path + test_file, x_function=self.x_transform_function, y_function=self.y_transform_function)
        elif self.x_transform_function is not None:
            base_dataset = CustomDataSet(test_file, test_file_path + test_file, x_function=self.x_transform_function)
        elif self.y_transform_function is not None:
            base_dataset = CustomDataSet(test_file, test_file_path + test_file, y_function=self.y_transform_function)
        else:
            base_dataset = CustomDataSet(test_file, test_file_path + test_file)                    
        return base_dataset
    
    def run_tests(self):
        for test_df_file in self.test_datasets:
            if self.name_in_path:
                test_file_path = "/".join(test_df_file.split("/")[:-1]) + "/"
                test_file = test_df_file.split("/")[-1]
                base_dataset = self.new_dataset(test_file, test_file_path)
            else:
                base_dataset = self.new_dataset(test_df_file, self.test_path)
            predictions = self.classification_pipeline.estimator.predict(base_dataset.x())
            if self.debug:
                print("test", test_df_file)
                print(predictions.shape)
                print(base_dataset.x().shape)
                print(base_dataset.y().shape)
            acc_score, recll_score, prec_score, score_f1 = self.get_scores(base_dataset.y(), predictions)
            self.save_test_result(base_dataset.name, acc_score, recll_score, prec_score, score_f1)
