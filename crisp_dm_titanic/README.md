# CRISP-DM • Titanic

Dataset: Kaggle *Titanic*.

## Kaggle download (in Colab)
1. Upload your `kaggle.json` (Kaggle API key) to Colab.
2. Then run the first cell in the notebook to download:
```
!pip install -q kaggle
!mkdir -p ~/.kaggle && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
!kaggle competitions download -c titanic -p data && unzip -o data/titanic.zip -d data
```
Alternatively, manually upload `train.csv`, `test.csv` to `data/`.

See `CRISP_DM_Titanic.ipynb` for the full walkthrough.
