import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def param_grid_evaluation(model, param_grid, metric):
    """
    plot the metric as a function of parameter grid values
    :param model: fit model with cv_results_ as attribute
    :param param_grid: dictionary of parameter grids used to train the model
    :return:
    """
    df_paramgrid = pd.DataFrame(model.cv_results_)
    params = ['param_' + x for x in list(param_grid.keys())]
    features = params + [metric]
    for i in features:
        plt.figure()
        sns.scatterplot(x=i, y=metric, data=df_paramgrid)
