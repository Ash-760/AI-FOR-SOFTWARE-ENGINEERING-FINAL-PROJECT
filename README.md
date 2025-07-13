# AI-FOR-SOFTWARE-ENGINEERING-FINAL-PROJECT REPORT

Title: Heart Disease Prediction Using Machine Learning Aligned with SDG 3
Student Name: [OREMO ASHLEY ACHIENG]
Course: AI for Software Engineering
Date: [7/13/2025]
1. Introduction
   
Heart disease remains one of the leading causes of death worldwide, contributing significantly to healthcare burdens globally. Early detection and timely intervention are critical to reducing mortality. This project applies machine learning to predict the presence of heart disease in individuals using clinical and demographic features. The project aligns with United Nations Sustainable Development Goal 3 (Good Health and Well-being) by promoting preventive healthcare and supporting early diagnosis through data-driven tools.

2. Problem Statement

Manual clinical diagnosis often requires significant time, resources, and medical expertise. With the availability of health records and advancements in machine learning, it is possible to develop predictive models that assist healthcare professionals in identifying high-risk patients.

Objective:

To build and evaluate predictive models that determine whether a person is likely to develop heart disease based on clinical and lifestyle features.

3. Dataset Overview

Source: Kaggle – Heart Failure Prediction Dataset
Records: 918
Features:
- Age, Sex
- Chest Pain Type, RestingBP, Cholesterol
- Fasting Blood Sugar, ECG Results, Max Heart Rate
- Exercise-Induced Angina, Oldpeak, ST Slope
- Target: HeartDisease (0 = No, 1 = Yes)

4. Methodology

4.1 Tools & Libraries:

- Python 3.13
- Pandas, Seaborn, Matplotlib
- scikit-learn

4.2 Preprocessing:

- Checked for missing values (none found)
- Encoded categorical features using get_dummies()
- Train/test split: 80% training, 20% testing

4.3 Models Used:

1. Logistic Regression (Baseline)
2. Random Forest Classifier (Better Accuracy)

5. Evaluation Metrics

- Accuracy
- Precision & Recall
- F1-Score
- ROC-AUC

6. Results

Logistic Regression:
- Accuracy: ~86%
- Moderate performance

Random Forest Classifier:
- Accuracy: ~90%
- AUC: 0.94
Most influential features: Age, ST_Slope_Flat, Oldpeak, ExerciseAngina_Yes, ChestPainType_ASY

Visualizations included: Class distribution, ROC curve, Feature importance, Correlation heatmap

7. SDG 3 Alignment

This project supports:
- Target 3.4: Reduce mortality from non-communicable diseases
- Target 3.d: Strengthen risk detection

By applying machine learning to predict heart disease, we help prioritize early diagnosis, reduce strain on healthcare systems, and promote AI-powered decision support.

8. Conclusion

The project shows the power of ML in healthcare, especially for early diagnosis in cardiology. Random Forests performed best. Future improvements:
- Larger datasets
- Deep learning
- Deploying as a web app

9. References

1. Kaggle Dataset: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
2. scikit-learn Documentation: https://scikit-learn.org
3. United Nations SDGs: https://sdgs.un.org/goals/goal3

Appendix A: Feature Importance (Top 5)

Feature              | Importance
---------------------|------------
Age                  | High
ST_Slope_Flat        | High
Oldpeak              | High
ExerciseAngina_Yes   | Medium
ChestPainType_ASY    | Medium

Appendix B: Confusion Matrix (Random Forest)
                 | Predicted No | Predicted Yes
-----------------|--------------|---------------
Actual No        |      TP      |      FP
Actual Yes       |      FN      |      TN


