# DS605 Lab 7: Image Representation, PCA, Eigenfaces and Face Recognition

**Student Name:** Rachit Zaveri  
**Student ID:** 202618015  
**Course:** DS605 – Fundamentals of Machine Learning

## 1. Project Overview

This lab explores image representation, dimensionality reduction, and face recognition using Principal Component Analysis (PCA) and the Eigenfaces approach. The experiment uses the AT&T ORL Face Database to study how high-dimensional face images can be represented using a smaller number of principal components while retaining important information.

The project also compares nearest-neighbor face matching with traditional machine learning classifiers trained on PCA-reduced features.

## 2. Dataset

The experiment uses the **AT&T ORL Face Database**, obtained from Kaggle.

- **Dataset:** [AT&T Database of Faces – Kaggle](https://www.kaggle.com/datasets/kasikrit/att-database-of-faces)
- **Total images:** 400
- **Number of subjects:** 40
- **Images per subject:** 10
- **Image dimensions:** 112 × 92 pixels
- **Features per image:** 10,304 grayscale pixel values

Each image is converted into a grayscale representation and flattened into a one-dimensional feature vector.

### Train-Test Split

A reproducible, subject-stratified split was used, with seven training images and three testing images per subject.

| Set | Images | Features per image |
|---|---:|---:|
| Training | 280 | 10,304 |
| Testing | 120 | 10,304 |

All 40 subjects are represented in both sets.

## 3. Methodology

### Part A: Image Representation

- Loaded the face images and converted them to grayscale.
- Examined image dimensions and pixel intensity values.
- Flattened each image into a feature vector.
- Constructed the image feature matrix and associated subject labels.
- Created a reproducible train-test split while preserving representation of
