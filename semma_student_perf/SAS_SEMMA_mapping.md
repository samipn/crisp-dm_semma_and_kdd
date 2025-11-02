# SAS SEMMA Mapping (Trial/Help)
- **Sample**: Use a Data Partition node (e.g., 60/20/20 stratified) or a Sample node.
- **Explore**: StatExplore + Multiplot to review distributions, missingness; Association/Variable Selection as needed.
- **Modify**: Impute node (median/mode), Transform Variables (binning, log), Replacement; create Interaction node if relevant.
- **Model**: Decision Tree, Neural Network, Regression, Gradient Boosting; set misclassification costs for class imbalance.
- **Assess**: Model Comparison node → ROC, Lift, KS; export score code (SCORE code node) for deployment.
