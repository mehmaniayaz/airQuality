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


def visualize_n_important_features(df, n, model, target):
    """

    :param df: dataframe that has been used for training
    :param n: the first n important features
    :param model: random forest model
    :param target: list target feature for model
    :return:
    """

    if not isinstance(target, list):
        raise
    dict_feature_importance = dict(zip(list(df.keys()), model.best_estimator_.feature_importances_))
    dict_feature_importance_sorted = {k: v for k, v in
                                      sorted(dict_feature_importance.items(), key=lambda item: item[1], reverse=True)}

    plt.figure()
    sns.pairplot(df[list(dict_feature_importance_sorted.keys())[0:n] + target])

    plt.figure(figsize=(12, 8))
    sns.heatmap(df[list(dict_feature_importance_sorted.keys())[0:n] + target].corr(), annot=True)
