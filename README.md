# Customer Churn Prediction for Olist

## Business Problem Understanding

### Business Context

Olist is a Brazilian e-commerce startup that enables small and medium-sized businesses to sell their products across multiple marketplaces through a single platform. It provides logistics support, marketing tools, and payment services to help sellers streamline operations and expand their reach.

In 2018, Brazil had approximately 210 million people, with over 150 million having internet access. Around 60% of these internet users made online purchases, contributing to an estimated $24 billion in e-commerce transactions. However, customer retention remains a major challenge in this competitive landscape. Studies show that acquiring a new customer can cost five times more than retaining an existing one, and improving retention by just 5% can boost profits by 25% to 95%.

Initially, Olist focused on aggressive customer acquisition but has since shifted towards retention strategies to enhance lifetime value (LTV) and long-term profitability. Data-driven insights are crucial to this shift, enabling Olist to identify at-risk customers and implement targeted marketing strategies. Given that re-engaging existing customers is 40% more cost-effective than acquiring new ones, a retention-focused approach helps optimize marketing spend while strengthening Olist’s position in Brazil’s e-commerce market.

### Problem Statement

Despite significant growth, Olist faces ongoing customer churn challenges. The average annual churn rate in e-commerce ranges from 20% to 25%, and without effective retention strategies, Olist risks losing substantial revenue.

Olist has successfully acquired over ninety thousand customers with an average acquisition cost of ~$104 per customer. However, initial data indicates that only 15–20% of these customers make repeat purchases, suggesting a churn risk of over 30%.

To mitigate this risk, Olist invests in customer retention efforts. However, not all customers have the same likelihood of churning, making a uniform approach inefficient. A data-driven strategy allows for targeted interventions, such as:

- Personalized promotions and discounts.
- Tailored product recommendations.
- Enhanced customer service and engagement initiatives.

By optimizing marketing spend and focusing on high-risk customers, Olist aims to increase repeat orders by at least 20%, improve retention rates, and maximize long-term revenue.

## Goals

To address customer churn, this study aims to develop a machine learning model that predicts the likelihood of churn based on historical transaction data. Key objectives include:

### Customer Behavior Analysis

- Identifying patterns in purchase frequency, spending habits, and inactivity periods.
- Determining key factors influencing customer churn.

### Churn Prediction Model Development

- Building a high-accuracy classification model to detect high-risk customers.
- Setting a target to reduce churn from the existing baseline.

### Marketing Cost Optimization

- Directing retargeting efforts toward high-risk customers.
- Reducing marketing costs per active customer by up to 30% compared to new customer acquisition costs.

### Actionable Insights for Retention Strategies

- Providing data-driven recommendations for personalized campaigns.
- Enhancing engagement strategies to boost repeat purchases and long-term retention.

---

## Churn Conceptualization

Since Olist is a relatively new e-commerce platform, defining churn should not solely be based on purchase frequency or days since last transaction. Most new customers only make a single purchase, making it more relevant to segment them into three groups to ensure a more accurate churn definition, we categorize it as follows:

- **One-Time Buyer:** If the customer does not make a second purchase within 6 months after their first purchase, they are considered churned.
- **Repeat Buyer:** If the customer does not make another purchase within 6 months after their last purchase, they are considered churned.
- **New Customer:** Since this segment consists of customers from the last 5 months, there is not yet enough data to determine churn. They have the potential to become repeat buyers, so further observation is necessary.

---

## Technical Approach

1. **Data Cleaning and Preprocessing:**

   - Translating, merging, and dropping unused columns.
   - Handling duplicate and missing data.
   - Formatting data and renaming columns.

2. **Exploratory Data Analysis (EDA) and Data Visualization**

3. **Churn Analysis**

4. **Data Preparation for Machine Learning**

5. **Model Development:**

   - Logistic Regression
   - K-Nearest Neighbors (KNN)
   - Decision Tree
   - Random Forest
   - AdaBoost
   - Gradient Boosting
   - Extreme Gradient Boosting (XGBoost)

6. **Hyperparameter Tuning**

   - Selecting the best two models from cross-validation.
   - Optimizing model parameters.

7. **Model Evaluation on Test Set:**

   - Before and after hyperparameter tuning.

8. **Performance Metrics:**

   - Precision and Recall Analysis
   - Feature Importance Analysis

9. **Conclusion and Recommendations**

---

## Data Information

- **Source:** Olist, and André Sionek (2018). Brazilian E-Commerce Public Dataset by Olist. Kaggle.
- **Dataset Link:** [Kaggle - Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Timeframe:** 2016–2018
- **Size:** Over 100,000 orders

---

## Tools and Technologies Used

### Programming Language

- Python

### Standard Libraries

- `numpy`, `pandas`: For data manipulation and analysis.
- `matplotlib`, `seaborn`: For data visualization.

### Machine Learning and Preprocessing

- `scikit-learn`:
  - `train_test_split`, `StratifiedKFold`, `GridSearchCV`, `RandomizedSearchCV`, `cross_val_score`: Model training and validation.
  - `ColumnTransformer`, `Pipeline`: Data preprocessing.
  - `OneHotEncoder`, `RobustScaler`: Encoding and scaling.
  - `IterativeImputer`: Handling missing values.
  - Evaluation metrics: `accuracy_score`, `recall_score`, `precision_score`, `f1_score`, `classification_report`, `roc_auc_score`, `PrecisionRecallDisplay`, `make_scorer`.
- `imbalanced-learn`: Handling imbalanced data using `SMOTE` and other techniques.
- `xgboost`: For building the Extreme Gradient Boosting classifier.

### Classifiers Used

- `LogisticRegression`
- `KNeighborsClassifier`
- `DecisionTreeClassifier` (with `plot_tree` for visualization)
- `RandomForestClassifier`
- `AdaBoostClassifier`
- `GradientBoostingClassifier`
- `XGBClassifier`

### Utilities

- `pickle`: Saving and loading the trained model.
- `os`: System-level file handling.
- `warnings`: For managing warning messages.

---
