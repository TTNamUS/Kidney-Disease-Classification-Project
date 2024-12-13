# Kidney Disease Classification
This project focuses on the classification of kidney diseases using deep learning and computer vision techniques. We have developed a complete pipeline encompassing data ingestion, transformation, model training, and evaluation. The project leverages technologies such as Next.js, TypeScript, TailwindCSS for the frontend, and Python, Fastapi, mlflow, DVC for the backend.

### Live URL: https://kidney-disease-classification-project.vercel.app/

## Features
- Comprehensive data processing and transformation pipeline.
- Multiple deep learning, Transformers and machine learning models for comparative analysis.
- Complete backend implementation in Fastapi with logging, custom exception handling, and class-based modular coding following OOPs principles.
- Frontend developed using Next.js, TailwindCSS, TypeScript and Shadcn.UI for a seamless user experience.

## Dataset Information

### Context
CT KIDNEY DATASET: Normal-Cyst-Tumor and Stone

### Content
The dataset comprises 12,446 unique data points, including 3,709 cyst, 5,077 normal, 1,377 stone, and 2,283 tumor findings. It was collected from PACS from various hospitals in Dhaka, Bangladesh. After thorough selection and anonymization processes, the images were converted to a lossless jpg format and verified by medical professionals.

### Dataset Link: https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone/data

## Technology Stack
### Frontend:
- Nextjs
- TypeScript
- TailwindCSS
- Shadcn.UI
### Backend:
- Python
- DVC
- MLFlow
- Deep Learning & Computer Vision
- Fastapi
- OOP Principles

### Models Trained
- VGG16

## My dagshub and mlflow
You can track the progress and results of the training pipeline using Dagshub for version control, pipeline visualization, and collaboration.  
My dagshub: https://dagshub.com/TTNamUS/Kidney-Disease-Classification-Project

Detailed metrics, parameters, and artifacts are logged and can be explored through the MLflow UI.  
My mlflow: https://dagshub.com/TTNamUS/Kidney-Disease-Classification-Project.mlflow

# How to run Backend?
### STEPS:

Clone the repository

```bash
git clone https://github.com/TTNamUS/Kidney-Disease-Classification-Project.git
```
### STEP 01- Create a Python environment after opening the repository

```bash
cd Kidney-Disease-Classification-Using-Deep-Learning
conda create -p venv python=3.10 -y
conda activate venv/
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run the Fastapi Backend
```bash
python app.py
```
or
```bash
uvicorn app:app --reload --port 8080
```

### STEP 04- Run the Training Pipeline
```bash
python main.py
```
or using DVC pipeline
```bash
dvc init
dvc repro
dvc dag
```
To launch the MLflow UI, use the command:
```bash
mlflow ui
```



# How to run Frontend?
### STEP 01- Go to client
```bash
cd frontend
```
### STEP 02- install the requirements
```bash
npm install
```

### STEP 03- Run the NextJS frontend
```bash
npm run dev
```

### STEP 04- Build the frontend
```bash
npm run build
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


## References
- https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
- https://github.com/Youssef22Ashraf/kidney_Disease-Classification-project
