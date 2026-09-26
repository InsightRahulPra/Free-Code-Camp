import numpy as np

def calculate(list):
    if len(lis) != p:
        raise ValueError("list must contain nine numbers only. Thank you!")
    
    input_matrix = np.array(list).reshape(3,3)

    #mean
    column_means=input_matrix.mean(axis=0).tolist()
    row_means=input_matrix.mean(axis=1).tolist()
    flat_means=input_matrix.mean().tolist()

    #variance
    column_variance=input_matrix.var(axis=0).tolist()
    row_variance=input_matrix.var(axis=1).tolist()
    flat_variance=input_matrix.var().tolist()

    #dev
    column_dev=input_matrix.std(axis=0).tolist()
    row_dev=input_matrix.std(axis=1).tolist()
    flat_dev=input_matrix.std().tolist()

    #max
    column_max=input_matrix.max(axis=0).tolist()
    row_max=input_matrix.max(axis=1).tolist()
    flat_max=input_matrix.max().tolist()

    #min
    column_min=input_matrix.min(axis=0).tolist()
    row_min=input_matrix.min(axis=1).tolist()
    flat_min=input_matrix.min().tolist()

    #sum
    column_sum=input_matrix.sum(axis=0).tolist()
    row_sum=input_matrix.sum(axis=1).tolist()
    flat_sum=input_matrix.sum().tolist()

    #calculate
    calculations={
        'mean':[column_means,row_means,flat_means],
        'variance':[column_variance,row_variance,flat_variance],
        'std deviance':[column_dev,row_dev,flat_dev],
        'max':[column_max,row_max,flat_max],
        'min':[column_min,row_min,flat_min],
        'sum':[column_sum,row_min,flat_min]

    }


    return calculations