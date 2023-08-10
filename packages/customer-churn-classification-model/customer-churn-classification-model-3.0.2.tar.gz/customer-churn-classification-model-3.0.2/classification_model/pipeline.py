# import packages and custom feature
# for building our models
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier

from classification_model.config.core import config
from classification_model.processing import custom_feature as cf

# set up the pipeline
customer_churn_pipeline = Pipeline(
    [
        # == CATEGORICAL ENCODING ======
        (
            "categorical_encoder",
            cf.CategoricalEncoder(variables=config.model_config.cat_vars),
        ),
        # # ==== FEATURE SELECTION ========
        # (
        #     "selected_features",
        #     cf.SelectedFeatures(variables=config.model_config.selected_features),
        # ),
        # ==== SCALING OUR data ========
        (
            "scaler",
            StandardScaler(),
        ),
        # final estimator
        (
            "xgb",
            XGBClassifier(
                eta=config.model_config.eta,
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
