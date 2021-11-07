import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from ._xy_dataset_return import no_transform_x
from ._xy_dataset_return import no_transform_y

def ripado():
    print("RIP")

class CustomDataSet:
    def __init__(self, name, dataset_file, test_size=0.3, 
                 class_column_name="Device Class", random_state=42, x_function=no_transform_x, y_function=no_transform_y, debug=False):
        self.name = name # Nome para aparecer no arquivo de resultados
        self.dataset = pd.read_csv(dataset_file) # proprio dataset
        self.return_x = x_function # funçao que retornara o x do dataset
        self.return_y = y_function # funçao que retornara a classo do dataset
        self.class_column = class_column_name # nome da coluna de class
        self.test_size = test_size # porcentagem que sera separada para teste
        self.random_state = random_state 
        self.debug = debug
        self.train_test_split()
        if self.debug:
            self.na_values()
            
    def na_values(self):
        print(self.name)
        aux_nan = (self.dataset.isna().sum()).sort_values()
        for column in self.dataset.columns:
            try:
                aux_inf = np.isinf(self.dataset[column]).values.sum()
                if aux_inf > 0:
                    print("inf:", column, aux_inf)
            except:
                print(column, "fail inf")
        print(aux_nan[lambda x: x > 0])
            
    # The ideai behind this function is to keep the transformation function
    def replace_dataset_df(self, new_name, new_file, test_size=0.3, class_column_name="Device Class", random_state=42):
        self.name = new_name
        self.dataset = pd.read_csv(new_file) # proprio dataset
        self.test_size = test_size
        self.train_test_split()
            
    def train_test_split(self):
        x_train, x_test, y_train, y_test = train_test_split(self.x(), self.y(), test_size=self.test_size)
        self.train_indexes = y_train.index.values.tolist()
        self.test_indexes = y_test.index.values.tolist()
        
    def x(self, train=False, test=False):
        if train:
            return self.return_x(self.dataset, self.class_column, rows=self.train_indexes)
        if test:
            return self.return_x(self.dataset, self.class_column, rows=self.test_indexes)
        return self.return_x(self.dataset, self.class_column)
    
    def y(self, train=False, test=False):
        if train:
            return self.return_y(self.dataset, self.class_column, rows=self.train_indexes)
        if test:
            return self.return_y(self.dataset, self.class_column, rows=self.test_indexes)
        return self.return_y(self.dataset, self.class_column)
