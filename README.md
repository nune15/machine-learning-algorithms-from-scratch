# ML Algorithms From Scratch

This folder contains implementations of core Machine Learning algorithms **from scratch** in Python.  
Each algorithm is implemented manually without using external ML libraries to help understand the underlying mechanics.

## 🔹 Algorithms Included

### 1. Decision Tree Classifier
- Implements classification using **Gini Index** splits.
- Supports both categorical and numerical features.
- Fully implemented manually to illustrate tree building and decision logic.

### 2. K-Nearest Neighbors (KNN)
- Classification based on **Euclidean distance**.
- Configurable K parameter.
- Demonstrates fundamental nearest neighbor classification logic.

### 3. Gini Index
- Core function for Decision Tree splits.
- Calculates dataset impurity step by step.
- Can be reused in other tree-based models.

---

## 📂 Structure

```text
ml-algorithms/
│
├── decision-tree/
│   └── decision_tree.py
├── knn/
│   └── knn.py
├── gini-index/
│   └── gini.py
└── README.md
