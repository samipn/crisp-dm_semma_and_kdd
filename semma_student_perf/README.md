# SEMMA • Student Performance

Dataset: Kaggle Student Performance (predict final grade / pass-fail).

Colab Kaggle download pattern (update dataset slug as needed):
```
!pip install -q kaggle
!mkdir -p ~/.kaggle && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
# Example (adjust slug to your chosen Student Performance dataset):
!kaggle datasets download -d joebeachcapital/students-performance -p data && unzip -o data/students-performance.zip -d data
```
Open `SEMMA_Student_Performance.ipynb` to follow SEMMA phases.
Also see `SAS_SEMMA_mapping.md` to replicate in SAS (trial).