from sklearn.metrics import mean_squared_error

def medir_uso_baseline(y_test, y_baseline_pred):
    """
    Mide el rendimiento del modelo utilizando un enfoque de baseline, comparando las predicciones del modelo con una referencia (ground truth) utilizando métricas como el error cuadrático medio (MSE).
    """

    baseline_mse = mean_squared_error(y_test, y_baseline_pred)
    print(f"MSE del Baseline (Promedio): {baseline_mse:.2f}")
