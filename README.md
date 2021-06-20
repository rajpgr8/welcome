
```
sudo apt update
sudo apt install python3-pip
sudo pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 src/app.py

docker build -t app-welcome .
docker-compose up --build
kubectl apply -f deployment.yml

docker tag app-welcome-image gcr.io/[PROJECT_ID]/[REPO_NAME]:latest
docker push gcr.io/[PROJECT_ID]/[REPO_NAME]:latest
```
