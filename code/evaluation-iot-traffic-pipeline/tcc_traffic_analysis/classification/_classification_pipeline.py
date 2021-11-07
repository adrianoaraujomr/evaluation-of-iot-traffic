import json
from joblib import dump, load
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from ..custom_algorithms import CustomAlgorithm

class ClassificationPipeline:
    def __init__(self, algorithm_name, classificador, dataset, parametros, scorers, 
                 refit="precision_score", feature_selection=None, normalization=None, debug=False):
        self.algorithm = algorithm_name # nome do algoritmo de classificação
        self.classifier = classificador # objeto classificador
        self.dataset = dataset # objeto dataset, CustomDataSet()
        self.parameters = parametros # parametro para grid search
        self.scorers = scorers # objetos para mediçao de performance para o grid search
        self.refit = refit
        self.feature_selection = feature_selection # objedto de feature selection, CustomFeatureSelection()
        self.normalization = normalization # objedto de normalizacao, CustomFeatureSelection()
        self.train_method = "" # vai salvar qual o metodo de treino usado no classificador gerado
        self.debug = debug
        self.prepare_pipeline()
        
    def get_model_name(self):
        return self.algorithm.lower().replace(" ", "_") + "_" + self.train_method.lower().replace(" ", "_") + "_" + self.feature_selection.name.lower().replace(" ", "_") + "_" + self.dataset.name.replace(".csv", ".sck").replace(" ", "_")
        
    def persist_model(self, model_dir):
        dump(self.estimator, model_dir + "/" + self.get_model_name())        
        
    def prepare_pipeline(self):
        steps = []        
        if self.normalization is not None:
            steps.append((self.normalization.name, self.normalization.algorithm))
        else:
            self.normalization = CustomAlgorithm("-", None)
        if self.feature_selection is not None:
            steps.append(('FSele', self.feature_selection.algorithm))
        else:
            self.normalization = CustomAlgorithm("-", None)
        steps.append(('Class', self.classifier))
        self.pipeline = Pipeline(steps)

    def train_holdout(self):
        self.train_method = "Holdout"
        if self.debug:
            print(self.train_method, self.dataset.name, self.feature_selection.name)
        self.pipeline.fit(self.dataset.x(train=True), self.dataset.y(train=True))
        self.estimator = self.pipeline
        
    def train_grid_search(self, cv_n_splits=3, cv_random_state=42, cv_jobs=1):
        self.train_method = "Grid Search " + str(cv_n_splits) + " folds"
        if self.debug:
            print(self.train_method, self.dataset.name, self.feature_selection.name)
        if self.parameters is not None:
            grid = GridSearchCV(self.pipeline, 
                                param_grid=self.parameters, 
                                cv=StratifiedKFold(n_splits=cv_n_splits), 
                                n_jobs=cv_jobs, 
                                scoring=self.scorers,  
                                refit=self.refit)
        else :
            grid = GridSearchCV(self.pipeline, 
                                cv=StratifiedKFold(n_splits=cv_n_splits), 
                                n_jobs=cv_jobs, 
                                scoring=self.scorers,  
                                refit=self.refit)
        grid.fit(self.dataset.x(), self.dataset.y())
        self.grid_best_score = grid.best_score_
        self.estimator = grid.best_estimator_
