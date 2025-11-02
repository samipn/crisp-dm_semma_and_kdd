from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def split_xy(df: pd.DataFrame, y_col: str):
    X = df.drop(columns=[y_col])
    y = df[y_col]
    return X, y

def basic_numeric_categorical_preprocessor(X: pd.DataFrame):
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = X.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
    numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    categorical_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    pre = ColumnTransformer(
        transformers=[("num", numeric_transformer, numeric_features), ("cat", categorical_transformer, categorical_features)]
    )
    return pre, numeric_features, categorical_features
