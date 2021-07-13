# Renewable Energy Prediction using Weather Data

This is my thesis work on renewable energy detection which compares state of art models using Machine Learning and Deep Learning adapted from multivariate time series weather data.

The data uses the weather data and renewable energy outputs from [Open Power System Data](https://open-power-system-data.org/) and I would also like to thank research scientists, study and data managers and developers who make the study possible. The data is freely accessible @https://open-power-system-data.org/

The study relied on Forecast and Observed Weather Data for analysis of this study. For which the Observed Weather Data was retrieved from [Open Power System Data](https://open-power-system-data.org/) and for Forecast Weather Data I relied on [Visual Crossing](https://www.visualcrossing.com/) which is a paid service.

The folder below contains the following models:

*-* **CNN + LSTM**

    Research Paper: Forecasting Solar Power Using Long-Short Term Memory and Convolutional Neural Networks

*-* **WD + LSTM**

    Research Paper: A Novel Deep Learning Approach for Wind Power Forecasting Based on WD-LSTM Model

*-* **DRNN**

    Research Paper: Deep Learning based Models for Solar Energy Prediction

*-* **Gaussian Mixture Density Network**

    Research Paper: A review and taxonomy of wind and solar energy forecasting methods based on deep learning

*-* **SVM + RBF Kernel**

    Research Paper: Predicting Solar Generation from Weather Forecasts Using Machine Learning

*-* **RFR (Forecast + Observed Data)**

    Research Paper: A Two-Step Approach to Solar Power Generation Prediction Based on Weather Data Using Machine Learning
 
*-* **SVR and DT Regressor ensemble**

    Research Paper: Machine Learning Ensembles for Wind Power Prediction
 
*-* **Stacking**: Stack different ML models that are best for the model and run predictions.

    Research Paper: Heuristic Approach using LazyPredict Python Package


It also contains a visualization of the intermediate activations learnt by the ResNet 2D model with CW for windowed data