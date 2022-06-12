# Start Machine Learning project.

# Software and account Requirement.
    1. Github Account
    2. Heroku Account
    3. VS Code IDE
    4. GIT cli

# Creating Conda Enviroment 

```
conda create -p venv python=3.7 -y

```
# Activating conda enviroment

```
conda activate venv\

```
# run the below commands to install dependecies 
```
pip install -r requirements.txt

```
# to add all files to git
```
git add .

```

# OR

```
git add <file-name>

```

# to check the git status
```
git status
```

# to check git logs
```
git log
```

# to create version/commit all changes to git
```
git commit -m "message"

```
# to push the changes to git
```
git push origin main

```

# Setting up CI/CD Pipeline 

1. HEROKU_EMAIL = xxxx@gmail.com
2. HEROKU_API_KEY = < api-key >
3. HEROKU_APP_NAME = ml-prj-demo

# Build Docker image 

```
docker build -t <image_name>:<tagname> . 
```

# to list the docker images 

```
docker images
```

# Run docker image 

```
docker run -p 5000:5000 -e PORT=5000 <image-from previous command> 
```

# to check running docker

```
docker ps 

```

# to stop docker 

```
docker stop <container-id>

```