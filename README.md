# Smart Grid Demand Response Analysis & Anomaly Detection using Machine Learning

## Problem Statement
Demand Response (DR) programs rely on accurate prediction of power consumption
patterns to balance supply and demand in smart grids. However, power
consumption data can be affected not only by natural behavioral variation,
but also by cyber-attacks targeting communication protocols used in smart
grid networks.

Network-specific protocol attacks such as MODBUS, TCP/IP, and WiMAX can
introduce anomalies in power consumption data, leading to incorrect demand
forecasts, financial losses, and reduced system reliability. Traditional
statistical approaches alone are often insufficient to capture these complex,
attack-induced deviations.

## Objective
To analyze demand response power consumption data and develop machine learning
and deep learning models for:
- Seasonal and temporal demand forecasting
- Identification of anomalous consumption patterns caused by network-specific
  protocol attacks
- Improving the reliability of demand response analytics in smart grid
  environments

## Approach
- Data cleaning and preprocessing of smart grid and demand response datasets
- Feature engineering on temporal, seasonal, and behavioral attributes
- Seasonal time-series modeling using ARIMA and SARIMA as statistical baselines
- Machine learning models for anomaly detection in power consumption patterns
- Correlation of detected anomalies with network-level protocol attacks
  (MODBUS, TCP/IP, WiMAX)
- Comparative evaluation of statistical, ML, and deep learning approaches

## Models Used
- ARIMA / SARIMA for seasonal demand forecasting
- Random Forest and tree-based models for anomaly detection
- Support Vector Machines (SVM) for classification of abnormal patterns
- Deep learning models: LSTM for modeling long-term temporal dependencies

## Results
- ARIMA and SARIMA models successfully captured seasonal power consumption
  trends and served as strong forecasting baselines
- Machine learning models identified abnormal consumption patterns associated
  with network-specific protocol attacks
- LSTM-based models improved detection of subtle and time-dependent anomalies
  in power usage behavior

## Tech Stack
- Programming: Python
- ML/DL: Scikit-learn, TensorFlow / PyTorch
- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn


## Context
This project was developed as part of my PhD research in applied machine
learning for smart grids, demand response, and cyber-physical system security.

## Reproducibility & Research Notes
- Experiments were conducted using publicly available and benchmark datasets
- Data preprocessing, feature extraction, and model training steps are documented
- Random seeds and model configurations are configurable for repeatability
- Results reported are based on multiple experimental runs

## Research Context
This work was conducted as part of my PhD research in Computer Engineering,
focusing on applied machine learning for energy systems and cyber-physical
system security.

Related peer-reviewed publications are listed in my CV.


## Author
**Rajesh Manicavasagam**  
Machine Learning Engineer | PhD in Computer Engineering (Applied Machine Learning)
GitHub: https://github.com/rmanicav
