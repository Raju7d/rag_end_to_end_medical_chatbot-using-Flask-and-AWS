# rag_end_to_end_medical_chatbot-using-Flask-and-AWS

# Problem statemet



# steps
1. Create a template.sh file and write the directory over there
2. Copy the Medical book to data folder
3. activate the virtual environment (python -m venv .venv) => .\.venv\Scripts\Activate
4. install the requirements.txt file ==> pip install requirements.txt
5. change the ipynb kernel to virtual environment kernel and start testing the coding in locally in jupyter file
6. Follow the Rag approach
    1. Load the data
    2. chunk it
    3. download the embeddings from huggingface or you can use paid embeddings model
    4. create a pinecone client
    5. create an index within the pinecone (Steps mentioned in trails.ipynb)
    6. store the embeddings in a pinecone vector db
    7. Create openai client and prompt template
    8. create a retriver
    9. retrive the relavant documents from the knowledge base
    10. pass that information to LLM
7. write a modular code in src
8. download or write the html and css code from the gooogle (free chatbot templates)
9. create an api's integrate them in a app.py
10. Run the app.py so that you can see the output in  localhost:8080 port

## Steps to follow deploy the application in AWS


# Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS

# How to run?
### STEPS:

Clone the repository

```bash
git clonehttps://github.com/entbappy/Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

IAM => users => create user => username => medical-chatbot => next => attach policies directly => AmazonEC2ContainerRegistryFullAccess ==> checkbox yes ==> add one more access => AmazonEC2FullAccess => next => create user

user will be created.

click on the user <medical-chatbot> => security credentials => access key => create access key => cli => add check box => next => create access key => copy the access key & secret  ==> download as csv file

# ECR SETUP

aws ==> search ==> ECR ==> elastic container repository => repository-name => medicalbot => create
save the uri => 349098282441.dkr.ecr.ap-south-1.amazonaws.com/medicalbot

# EC2 setup

aws ==> search ==> ec2 ==> launch instance => ubintu => instance type => t2.large (8gb memory or free )=> create a key pair => medical-chatbot => select http https 3 check boxes select => configure storage => 30 gb => launch instance =>view all instances

connect => connect ==> blank terminal will open try to run below commands

sudo apt-get update -y
sudo apt-get upgrade
docker --version
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh


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
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

	
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
	

# Github actions config
go to your repo ==> settings==> actions ==> runners=> new self hosted runner => Linux =>

copy the commands and execute in ec2 instance terminal

copy and paste the one by one command until configure command

then give runner name as self-hosted

enter

name of the work folder name: enter

execute the below command: ./run.sh

now add the environmental variables in a github
=================================================
secrets and variables ==> action => repository secrets =>new repository secret => 




# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY

