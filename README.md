# Student Performance Prediction Model

A machine learning model that predicts student performance in mathematics based on various demographic, social, and school-related factors using the Student Performance Dataset.

## 📋 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a Random Forest Regression model to predict student final grades (G3) in mathematics. The model analyzes various student attributes including demographic information, family background, social factors, and previous academic performance to make accurate predictions.

The project aims to help educators and institutions identify students who might need additional support and understand the key factors that influence academic performance.

## 📊 Dataset

The project uses the **Student Performance Dataset** from the UCI Machine Learning Repository, specifically focusing on mathematics performance (`student-mat.csv`).

### Dataset Information:
- **Source**: UCI Machine Learning Repository
- **Students**: 395 students
- **Features**: 33 attributes (32 features + 1 target)
- **Target Variable**: G3 (final grade, numeric: from 0 to 20)

### Key Attributes:
- **Demographic**: age, sex, address (urban/rural)
- **Family**: family size, parents' education and jobs, family relationships
- **School**: school choice, travel time, study time, failures, extra support
- **Social**: going out with friends, alcohol consumption, health status
- **Academic**: previous grades (G1, G2), absences, extra activities

## ✨ Features

- **Data Preprocessing**: Automatic encoding of categorical variables
- **Machine Learning**: Random Forest Regression for robust predictions
- **Model Persistence**: Trained model saved for future use
- **Scalable Architecture**: Easy to extend and modify

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   - Download `student-mat.csv` from [UCI Repository](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
   - Place it in the project root directory

## 🚀 Usage

### Training the Model

Run the main script to train and save the model:

```bash
python train_model.py
```

This will:
1. Load and preprocess the student performance data
2. Encode categorical variables
3. Split data into training and testing sets
4. Train a Random Forest Regression model
5. Save the trained model as `model.pkl`


## 🤖 Model Details

### Algorithm: Random Forest Regression

### Model Configuration:
- **Random State**: 42 (for reproducibility)
- **Train/Test Split**: 80/20

### Performance Metrics:
The model can be evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score
- Root Mean Squared Error (RMSE)

## 📁 Project Structure

```
student-performance-prediction/
├── model.pkl               # Trained model (generated)
├── data/                  # Data directory
│   └── student-mat.csv    # Dataset
├── model.py                # Model training utilities
└── app.py                  # Prediction utilitie
```

## 📈 Results

### Feature Importance
The Random Forest model provides insights into which factors most strongly influence student performance:

1. **Previous Grades (G1, G2)**: Strongest predictors
2. **Study Time**: Positive impact on performance
4. **School Support**: Important for at-risk students


*Note: Run the model to get actual performance metrics*


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## 📄 License

This project is licensed under the MIT License 

## 🙏 Acknowledgments

- **Dataset**: UCI Machine Learning Repository
- **Original Study**: P. Cortez and A. Silva. "Using Data Mining to Predict Secondary School Student Performance"
- **Libraries**: scikit-learn, pandas, numpy


⭐ **Star this repository if you find it helpful!**
