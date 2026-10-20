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
| Training | 280 | 10,304 |
| Testing | 120 | 10,304 |

All 40 subjects are represented in both sets.

## 3. Methodology

### Part A: Image Representation

- Loaded the face images and converted them to grayscale.
- Examined image dimensions and pixel intensity values.
- Flattened each image into a feature vector.
- Constructed the image feature matrix and associated subject labels.
- Created a reproducible train-test split while preserving representation of every subject.

### Part B: PCA and Eigenfaces

- Calculated the mean face from the training images.
- Centered the training and testing data using the training mean.
- Implemented PCA using covariance-based eigendecomposition and Singular Value Decomposition (SVD) with NumPy.
- Compared the eigenvalues and principal directions obtained using both methods.
- Calculated cumulative explained variance and visualized eigenfaces.
- Projected images into a lower-dimensional feature space.
- Reconstructed face images from their PCA representations and evaluated reconstruction error.

**Key PCA result:** 92 principal components retained approximately 90.04% of the training-data variance, reducing the representation from 10,304 pixel features to 92 PCA features per image.

### Part C: Nearest-Neighbor Face Recognition

Nearest-neighbor matching was implemented using Euclidean distance. Each test image was assigned the subject label of its closest training image.

The experiment compared recognition using:

1. Original pixel representations.
2. PCA-reduced representations using 92 components.

### Part D: Traditional Classifier Comparison

The following classifiers were trained and evaluated using PCA features:

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Support Vector Machine (SVM) with an RBF kernel

Different PCA component counts and KNN settings were also evaluated to examine their effect on classification accuracy.

## 4. Experimental Results

### PCA and Reconstruction

| Metric | Result |
| Original features per image | 10,304 |
| PCA components for at least 90% variance | 92 |
| Explained variance with 92 components | 90.04% |
| Reconstruction MSE | 335.52 |
| Reconstruction RMSE | 18.32 |
| Reduction in per-image feature values using 92 components | 99.11% |

The feature-value reduction compares the number of values used to represent each image. It does not include the storage required for the shared PCA basis and mean face.

### Face Recognition and Classifier Performance

The following results were obtained on the same test split of 120 images.

| Method | PCA components | Accuracy |
| Nearest Neighbor – Original Pixels | Not applicable | 97.50% |
| Nearest Neighbor – PCA Features | 92 | 97.50% |
| KNN (k = 1) | 92 | 97.50% |
| KNN (k = 3) | 92 | 90.83% |
| Logistic Regression | 92 | 99.17% |
| SVM (RBF kernel) | 92 | 98.33% |

Logistic Regression achieved the highest accuracy among these tested configurations, correctly classifying 119 out of 120 test images.

In the component-count experiments, Logistic Regression also achieved 99.17% accuracy with 20 PCA components, corresponding to approximately a 99.81% reduction in per-image feature values.

These results describe the tested configurations and split; they do not guarantee the same performance on other datasets or splits.

## 5. Visualizations

The repository includes the following generated plots:

- **`eigenfaces.png`** – Visualization of principal components represented as eigenfaces.
- **`reconstruction.png`** – Reconstructed face images using PCA representations.
- **`classifier_comparison.png`** – Comparison of classifier performance across tested configurations.

These visualizations help illustrate the effects of dimensionality reduction, image reconstruction, and classifier selection.

## 6. Technologies Used

- Python
- NumPy
- Matplotlib
- Pillow
- scikit-learn

NumPy was used for matrix operations, covariance-based eigendecomposition, SVD, PCA projections, and reconstruction. Matplotlib was used for visualization. scikit-learn was used for the traditional classification models.


### Dataset Setup

1. Download the [AT&T ORL Face Database from Kaggle](https://www.kaggle.com/datasets/kasikrit/att-database-of-faces).
2. Extract the dataset.
3. Place the `att_faces` directory in the location expected by the notebook.
4. If necessary, update the dataset path in the notebook to match your local directory.

## 8. Conclusion

This lab demonstrates how PCA can reduce the dimensionality of face-image data while preserving a substantial amount of its variance. The covariance-based eigendecomposition and SVD approaches produced consistent principal directions and eigenvalues within numerical precision.

Using 92 components retained approximately 90.04% of the variance, while nearest-neighbor recognition achieved 97.50% accuracy on both original pixel features and PCA-reduced features. Logistic Regression achieved 99.17% accuracy with the tested PCA representations, including a configuration with only 20 components.

Overall, the experiments illustrate the usefulness of dimensionality reduction for compact image representation and the importance of evaluating classification performance separately from explained variance.

## 9. Repository Contents

- `202618015_LAB7.ipynb` – Main notebook containing the implementation, experiments, and results.
- `eigenfaces.png` – Eigenface visualization.
- `reconstruction.png` – PCA reconstruction visualization.
- `classifier_comparison.png` – Classifier performance comparison.
- `.gitignore` – Excludes the local dataset directory and temporary files from Git tracking.

The dataset is not included in the repository and should be downloaded separately from Kaggle.

