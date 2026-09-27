# Linear and Logistic Regression - From Scratch and Optimization

## Overview

In this project, I worked with a garment industry productivity dataset to understand how Linear Regression and Logistic Regression work in practice.

First, I implemented both models using Scikit-learn and used them as a reference. After that, I implemented the models myself using NumPy, without using Scikit-learn for the actual model calculations. Finally, I tried to improve the scratch implementations by experimenting with different approaches and checking whether the changes actually improved the results.

For Linear Regression, the aim was to predict `actual_productivity`.

For Logistic Regression, I created a binary target called `MeetsTarget`, which tells whether the actual productivity reached the targeted productivity.

The complete process included data preprocessing, feature preparation, train-test splitting, model implementation, evaluation, and optimization.

## Key Observations

- The dataset contains **1197 records** and **16 columns**. During the initial data checking, there were no duplicate rows or missing values.

- The `MeetsTarget` classification variable is not perfectly balanced. Around **73.10%** of the records belong to class `1`, while around **26.90%** belong to class `0`.

- The data was divided into **957 training samples** and **240 testing samples**. The class proportions in the training and testing sets were also quite similar.

- For Linear Regression, the scratch implementation gave almost exactly the same results as the Scikit-learn implementation. The obtained values were approximately **0.1073 MAE, 0.1437 RMSE, and 0.2885 R²**.

- I then optimized the Linear Regression implementation by replacing the explicit pseudo-inverse calculation with NumPy's `lstsq()` function. The prediction results remained almost unchanged, while the measured training time became lower.

- For Logistic Regression, I implemented the sigmoid function and gradient descent manually. The initial scratch model achieved around **73.75% accuracy** and an **83.64% F1-score**.

- I experimented with different learning rates for the Logistic Regression model: `0.001`, `0.005`, `0.01`, `0.05`, and `0.1`.

- Among the learning rates that I tested, **0.005 gave the highest accuracy and F1-score**. The accuracy was about **74.17%** and the F1-score was about **84.18%**.

- The optimized Logistic Regression also achieved a recall of about **92.86%**, meaning that it correctly identified most of the positive `MeetsTarget` cases in the test data.

- One important thing I noticed during the experiments is that a lower training loss does not always mean better test performance. For example, some higher learning rates produced slightly lower training loss but their classification metrics on the test data were lower.

- Overall, implementing the models from scratch helped me understand what happens behind the Scikit-learn functions. The optimization experiments also showed that changing the implementation or hyperparameters should be based on actual results rather than just assuming that a change will make the model better.
