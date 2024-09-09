# model_explainability.py
import shap
import numpy as np

def explain_model(model, background_data, data_to_explain):
    explainer = shap.KernelExplainer(model.predict, background_data)
    shap_values = explainer.shap_values(data_to_explain)
    shap.summary_plot(shap_values, data_to_explain)
