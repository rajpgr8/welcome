
```
sudo apt update
sudo apt install python3-pip
sudo pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 src/app.py

pytest:
---------
virtualenv -p python3 venv
source venv/bin/activate
pip3 install pytest
pytest -v -s --junit-xml=report.xml

docker build -t app-welcome .
docker-compose up --build
kubectl apply -f deployment.yml
watch kubectl get pods,deployments,services

docker tag welcome_image gcr.io/[PROJECT_ID]/welcome_image:latest
docker push gcr.io/[PROJECT_ID]/welcome_image:latest
docker run -p 9091:9091 gcr.io/[PROJECT_ID]/welcome_image:latest

helm create my-app
helm lint my-app
helm package my-app
helm chart push [Artifactory REPO]

```
