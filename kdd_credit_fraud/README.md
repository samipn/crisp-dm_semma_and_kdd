# KDD • Credit Card Fraud

Dataset: Kaggle *Credit Card Fraud Detection (European cardholders, 2013)*.

Colab quickstart (after adding Kaggle API key):
```
!pip install -q kaggle
!mkdir -p ~/.kaggle && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d mlg-ulb/creditcardfraud -p data && unzip -o data/creditcardfraud.zip -d data
```
Then open `KDD_Credit_Fraud.ipynb`.
