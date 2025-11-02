# Data Science Methodologies Suite (CRISP-DM, KDD, SEMMA)

> Three end-to-end, real-world ML projects—each executed under a different methodology to compare workflows side-by-side and make them reproducible for study and reuse.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](#)
[![Notebooks: Colab-ready](https://img.shields.io/badge/Notebooks-Colab--ready-blue)](#)

---

## What's inside

Each subfolder is a **standalone project** following a specific methodology and dataset:

- `crisp_dm_titanic/` — **CRISP-DM** using the Kaggle *Titanic* classification problem.  
- `kdd_credit_fraud/` — **KDD** using the Kaggle *Credit Card Fraud* dataset.  
- `semma_student_perf/` — **SEMMA** using the Kaggle *Student Performance* dataset.  

Every project includes:

- A **Colab-ready notebook** that walks through all phases with **checklists**.
- A minimal **FastAPI** service under `deployment/api/` exposing `POST /predict`.
- A draft **article** in `medium_article.md` summarizing the project.
- A project-scoped **`requirements.txt`**.
- Optional **Dockerfile** under `docker/` for containerized runs.

> Datasets are not checked in. Use the Kaggle API or upload CSVs in Colab. See each project’s README/notebook cells for dataset instructions.

---
