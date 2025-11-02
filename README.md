# Data Science Methodologies Suite (CRISP-DM, KDD, SEMMA)

> Three end-to-end, real-world ML projects—each executed under a different methodology to compare workflows side-by-side and make them reproducible for study and reuse.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](#)
[![Notebooks: Colab-ready](https://img.shields.io/badge/Notebooks-Colab--ready-blue)](#)

---

## Walkthrough Video Link: https://drive.google.com/file/d/1GmRuoeqzgEP6NKYE3-2glA1iXnIVD87J/view?usp=sharing

## CRISP-DM: From Zero to Production on Titanic Dataset Medium Article: https://medium.com/@samiprichardniraula/crisp-dm-from-zero-to-production-on-titanic-dataset-d37357645e6b 

## KDD: Credit Card Fraud Detection Model (Kaggle) Medium Article: https://medium.com/@samiprichardniraula/kdd-credit-card-fraud-detection-model-kaggle-bc59c498c710 

## SEMMA End-to-End: Student Performance (Kaggle) Medium Article: https://medium.com/@samiprichardniraula/semma-end-to-end-student-performance-kaggle-17e0c8ba0aad

---

## What's inside

Each subfolder is a **standalone project** following a specific methodology and dataset:

- `crisp_dm_titanic/` — **CRISP-DM** using the Kaggle *Titanic* classification problem.  
- `kdd_credit_fraud/` — **KDD** using the Kaggle *Credit Card Fraud* dataset.  
- `semma_student_perf/` — **SEMMA** using the Kaggle *Student Performance* dataset.  

Every project includes:

- A **Colab-ready notebook** that walks through all phases with **checklists**.
- A minimal **FastAPI** service under `deployment/api/` exposing `POST /predict`.
- A project-scoped **`requirements.txt`**.
- Optional **Dockerfile** under `docker/` for containerized runs.

> Datasets are not checked in. Use the Kaggle API or upload CSVs in Colab. See each project’s README/notebook cells for dataset instructions.

---
