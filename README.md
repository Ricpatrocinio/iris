# Iris Prediction Model with CI/CD Pipeline

This repository contains an Iris prediction model with a complete CI/CD pipeline setup using GitHub Actions, AWS S3, and a simple Flask application.

## Project Structure

├── .github
│ └── workflows
│ └── main.yml
├── iris3.csv
├── Iris.ipynb
├── train_model.py
├── requirements.txt
├── README.md
├── index.html
├── script.js
├── app.py
└── model.pkl

bash


## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Ricpatrocinio/iris.git
cd iris
2. Install Dependencies
Ensure you have Python and pip installed.

sh

pip install -r requirements.txt
3. Train the Model
Run the training script to generate the model.

sh

python train_model.py
4. Run the Flask App
Start the Flask application.

sh

python app.py
5. Front-End Setup
Open index.html in a web browser to interact with the model.

CI/CD Pipeline
GitHub Actions Workflow
The CI/CD pipeline is set up using GitHub Actions. It includes the following steps:

Checkout code
Set up Python environment
Install dependencies
Install AWS CLI
Run training script
Deploy model to AWS S3
Run Flask app
AWS S3 Bucket
The model is uploaded to an S3 bucket named iris-model-bucket in the us-east-2 region. Ensure you have set up your AWS credentials as GitHub secrets:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
Workflow File: .github/workflows/main.yml
yaml

Triggering the Workflow
Push changes to the main branch to trigger the workflow:

sh

git add .
git commit -m "Trigger CI/CD pipeline"
git push origin main
Monitoring Workflow
Monitor the GitHub Actions tab to ensure the workflow runs successfully.Trigger CI/CD pipeline. v4
