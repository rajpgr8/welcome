
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
watch kubectl get pods,deployments,services

docker tag welcome_image gcr.io/[PROJECT_ID]/welcome_image:latest
docker push gcr.io/[PROJECT_ID]/welcome_image:latest
docker run -p 9091:9091 gcr.io/[PROJECT_ID]/welcome_image:latest

helm create my-app
helm lint my-app
helm package my-app
helm chart push [Artifactory REPO]


pytest:
---------
virtualenv -p python3 venv
source venv/bin/activate
pip3 install pytest
pytest -v -s --junit-xml=report.xml           (run all test cases in all files)
pytest -v -s -k 1st --junit-xml=report.xml    (run only test cases having '1st' in the test case name in the all test files)  -k <>
pytest -v -s -m smoke --junit-xml=report.xml  (run only test cases maked as 'smoke' in the all test files) -m <>
Note 1: 'test_1stTest_4' will always be skipped
Note 2: fixture method setup() defined in conftest.py file will always be executed fisrt before the test related to that fixture, 
        so setup() method will be executed befote 'test_1stTest_fistureTest' test run.
```
