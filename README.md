# CI/CD Setup Exercise for Iris Classification Model

This repository contains an exercise to set up Continuous Integration and Continuous Deployment (CI/CD) for a simple classification model using the Iris dataset. The project includes a Jupyter Notebook, Python scripts, and a configuration for GitHub Actions to automate the CI/CD pipeline.

## Project Structure

├── iris3.csv
├── Iris.ipynb
├── train_model.py
├── requirements.txt
├── README.md
└── .github
└── workflows
└── main.yml


### Files Description

- `iris3.csv`: The dataset file containing the Iris data.
- `Iris.ipynb`: Jupyter Notebook for data exploration and initial model training.
- `train_model.py`: Python script for training the Random Forest model and saving it as `model.pkl`.
- `requirements.txt`: List of dependencies required for the project.
- `README.md`: This file, explaining the project and CI/CD setup.
- `.github/workflows/main.yml`: GitHub Actions workflow file for automating CI/CD.

## CI/CD Pipeline Setup

### Step 1: Organize the Project Repository

1. **Create a GitHub Repository**: Create a new repository on GitHub.
2. **Add Files**: Add the project files (`iris3.csv`, `Iris.ipynb`, `train_model.py`, `requirements.txt`, and README.md) to the repository.

### Step 2: Convert Notebook to Script

The `train_model.py` script includes:
- Loading the dataset
- Preprocessing
- Model training
- Model saving

### Step 3: Create `requirements.txt`

List of dependencies:

pandas
scikit-learn
joblib


### Step 4: GitHub Actions for CI/CD

Create the GitHub Actions workflow file at `.github/workflows/main.yml`.

Step 5: AWS Setup
Create an S3 Bucket: Create an S3 bucket to store your model file.
Configure AWS CLI: Ensure AWS CLI is configured with the necessary permissions.
Step 6: CI/CD Execution
Push Code Changes: Commit and push your code to the GitHub repository.
Trigger Workflow: The GitHub Actions workflow will automatically run, training your model and deploying it to AWS S3.
Step 7: Monitor and Maintain
Monitor Workflow: Check the GitHub Actions tab in your repository to monitor the CI/CD process.
Update as Needed: Make necessary updates to your pipeline as your project evolves.

