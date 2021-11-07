import pandas as pd

class ManualFeatureSelection:
    def __init__(self, metric, num_features_keep, debug=False):
        columns_scores = pd.read_csv("./features_df.csv") # Score of columns based on metrics
        self.columns_to_keep = columns_scores.sort_values(by=[metric], ascending=False)['Colunas'].head(num_features_keep).values.tolist()
        self.num_features_keep = num_features_keep
        self.metric = metric
        self.debug= debug

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        if self.debug:
            print("transforming x,", self.metric, self.num_features_keep)
            print(X.shape)
            print(self.x.loc[:, self.columns_to_keep].values.shape)
        # maybe return the .values
        return X.loc[:, self.columns_to_keep].values
