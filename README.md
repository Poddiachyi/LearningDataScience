# Algorithms/methods:

Here are all the algorithms, methods and tasks I have implemented while learning data science.

### 1. Linear regression.
In the project there are also Gradient descent, R square and Regularization.
An example perfectly shows setbacks of Linear regression and Gradient descent which reaches a local minimum in this particular case.
Comparison to sklearn: on average my Linear regression works worse as a result of Gradient descent.

### 2. Logistic regression.
In the project there are also Gradient descent and Regularization.
An example perfectly works as a result of Gradient descent which reaches the global minimum.
Comparison to sklearn: on average my Logistic regression works as well as the implementation in sklearn.

### 3. Naive Bayese Classifier.
Comparison to sklearn: on average my Naive Bayese Classifier works as well as the implementation in sklearn.

### 4. Neural network.
A simple neural network for digits recognition with MNIST dataset.

### 5. KMeans.
Comparison to sklearn: on average my KMeans works as well as the implementation in sklearn.

### 6. PCA.
Comparison to sklearn: on average my PCA works as well as the implementation in sklearn, though my implementation is a bit slower.

### 7. SVM.
I used special library for convex optimization.
Comparison to sklearn: on average my SVM works worse as optimization is not good.

### 8. CNN.
Task: Classification and regression with Brazilian coin images
Link: https://www.kaggle.com/lgmoneda/br-coins

For the regression task I have added my own metric. Cents metric shows mean error in cents. For instance, y_true = [100, 50, 5], y_pred = [93, 54, 4]. At first I round results to five (as five is the smallest value), so now y_pred = [95, 55, 5]. Now I take abs of errors which gives [5, 5, 0]. So mean error is 3.33 cent. It gives better understanding of what is going on.
# LearningDataScience
