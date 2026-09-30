## Overview

This lab focuses on applying machine learning techniques to two different types of data: images and text.

For the image classification task, an asphalt crack dataset was used. OpenCV was used for image processing and feature extraction. Instead of directly feeding the images into a model, different numerical features were extracted from the images and then used for classification.

For the text classification task, an email dataset was used to classify emails as Spam or Non-Spam.

The main objective of the lab was to understand how preprocessing, feature representation, model selection, and evaluation affect the performance of machine learning models.

---

## Part A: Image Classification

The image dataset contains two classes:

- Crack
- NonCrack

There are 400 images in total, with 200 images belonging to each class.

### Image Preprocessing

OpenCV was used for processing the images. The images were converted from RGB/BGR format to grayscale before extracting numerical features.

The following features were extracted:

- Mean brightness
- Contrast
- Dark pixel ratio
- Bright pixel ratio
- Edge count
- Edge density

## Machine Learning Models

Three classification models were evaluated:

1. Logistic Regression
2. Decision Tree
3. K-Nearest Neighbors (KNN)

The dataset was divided into 80% training data and 20% testing data.

### Initial Model Results

| Model | Test Accuracy |

| Logistic Regression | 86.25% |
| Decision Tree | 86.25% |
| KNN | 90.00% |

KNN initially performed better than the other two models.

## KNN Hyperparameter Selection

Different values of K were tested:

| K | Test Accuracy |

| 1 | 93.75% |
| 3 | 91.25% |
| 5 | 90.00% |
| 7 | 88.75% |
| 9 | 90.00% |
| 11 | 88.75% |
| 15 | 87.50% |

Five-fold cross-validation was then used to select K more reliably.

| K | Mean CV Accuracy |

| 1 | 94.375% |
| **3** | **95.625%** |
| 5 | 95.000% |
| 7 | 93.438% |
| 9 | 92.500% |
| 11 | 92.188% |
| 15 | 92.500% |

Based on cross-validation, K = 3 was selected.

The final KNN model achieved:

**Test Accuracy: 91.25%**

Confusion Matrix:

```text
[[37  3]
 [ 4 36]]
```

# Part B — Email Spam Classification

## 1. Dataset

The second part of the lab focuses on classifying emails into two categories:

- Spam
- Non-Spam

The dataset contains:

- 5172 emails
- 3000 numerical features
- 3672 Non-Spam emails
- 1500 Spam emails

The target variable is `Prediction`, where:

- `0` represents Non-Spam
- `1` represents Spam

## 2. Data Preparation

Before training the model, the dataset was checked for missing values.

No missing values were found in the dataset.

The class distribution was also examined. The dataset contains more Non-Spam emails than Spam emails, so the classes are not perfectly balanced.

The dataset was divided into training and testing sets using an 80:20 split.

The resulting datasets were:

- Training set: 4137 samples
- Testing set: 1035 samples

The training set contained:

- 2937 Non-Spam emails
- 1200 Spam emails

The testing set contained:

- 735 Non-Spam emails
- 300 Spam emails

## 3. Text Representation

The dataset already contains 3000 numerical word-based features.

These features were directly used for classification.

TF-IDF vectorization was skipped as required for this lab.

## 4. Logistic Regression

Logistic Regression was used to classify the emails as Spam or Non-Spam.

The model was trained on the training set and evaluated on the test set using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 5. Results

The Logistic Regression model achieved an accuracy of:

**98.26%**

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| Non-Spam | 0.99 | 0.98 | 0.99 | 735 |
| Spam | 0.96 | 0.98 | 0.97 | 300 |
| **Overall Accuracy** | | | **0.98** | **1035** |

### Confusion Matrix

```text
[[722  13]
 [  5 295]]
```

# Part C — Improving Image Representation

## 1. Objective

The objective of this part was to investigate whether changing the image representation could improve the performance of the image classification model.

The Canny edge detection method was used for this experiment.

## 2. Original Representation

In the original image representation, Canny edge detection was performed using:

- Lower threshold: 50
- Upper threshold: 150

These thresholds were used to generate the `edge_count` and `edge_density` features.

## 3. Modified Representation

The Canny thresholds were changed to:

- Lower threshold: 30
- Upper threshold: 100

Lower thresholds make the edge detector more sensitive to weaker intensity changes. The purpose of this experiment was to check whether detecting additional edges could provide more useful information for distinguishing Crack and NonCrack images.

The remaining image features and the KNN model were kept unchanged so that the effect of changing the image representation could be compared fairly.

## 4. Experimental Setup

The original and modified representations were evaluated using the same KNN model with:

- K = 3
- Same train-test split
- Same six-feature structure
- StandardScaler before KNN

Only the Canny thresholds used to generate the edge features were changed.

## 5. Results

| Representation | Canny Thresholds | K | Accuracy |
|---|---|---:|---:|
| Original | (50, 150) | 3 | 91.25% |
| Modified | (30, 100) | 3 | 91.25% |

### Original Confusion Matrix

```text
[[37  3]
 [ 4 36]]
```

Observations: 

The modified Canny thresholds changed the edge representation of the images by making the edge detector more sensitive to weaker intensity changes.

However, the final KNN test accuracy remained unchanged at 91.25%.

The confusion matrix also remained the same for both representations.

Therefore, the modified Canny thresholds did not produce a measurable improvement in classification performance for this dataset and train-test split.

Conclusion:

Changing the Canny thresholds from (50, 150) to (30, 100) was tested as a possible improvement to the image representation.

Although the extracted edge features changed, the classification accuracy remained the same.

This experiment shows that changing the feature representation does not necessarily lead to better model performance. The usefulness of a representation change needs to be evaluated using the actual classification results.
