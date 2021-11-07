def no_transform_x(dataset, column_name, rows=None):
    if rows is not None:
        return dataset.drop([column_name], axis=1).iloc[rows]
    else:
        return dataset.drop([column_name], axis=1).iloc[:]

def no_transform_y(dataset, column_name, rows=None):
    if rows is not None:
        return dataset[column_name].iloc[rows]
    else:
        return dataset[column_name]
