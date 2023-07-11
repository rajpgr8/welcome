
##### k3d local development : Create virtual env, build/push/run image
```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
sudo virtualenv venv 
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
```

```
pytest:
---------
virtualenv -p python3 venv
source venv/bin/activate
pip3 install pytest
pip3 install pytest-html
pytest -v -s --junit-xml=report.xml  --html=report.html     (run all test cases in all files)
pytest -v -s -k 1st --junit-xml=report.xml    (run only test cases having '1st' in the test case name in the all test files)  -k <>
pytest -v -s -m smoke --junit-xml=report.xml  (run only test cases maked as 'smoke' in the all test files) -m <>
Note 1: 'test_1stTest_4' will always be skipped
Note 2: fixture method setup() defined in conftest.py file will always be executed fisrt before the test related to that fixture, 
        so setup() method will be executed befote 'test_1stTest_fistureTest' and 'test_2ndTest_2' test run.
        similarly we can wrap all tests (which are dependent on fixture method) into a class (see test_app3.py) and mark that class as usefixtures.
Note 3: we can pass data from fixture method also we can parametrize our test case (see conftest.py and test_app3.py)
```

##### k3d local development : Install K3D, kubectx, kubens, Create K3D cluster, Create local registry, Create virtual env, Build/push/run image 
```
sudo git clone https://github.com/ahmetb/kubectx /opt/kubectx
sudo ln -s /opt/kubectx/kubectx /usr/local/bin/kubectx
sudo ln -s /opt/kubectx/kubens /usr/local/bin/kubens
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
k3d registry create mycluster-registry --port 5000
k3d cluster create mycluster --registry-use mycluster-registry:5000
echo "alias k=kubectl" >> ~/.bashrc
source <(kubectl completion bash) 
echo "source <(kubectl completion bash)" >> ~/.bashrc
source ~/.bashrc
sudo su -
echo "127.0.0.1 k3d-mycluster-registry" >> /etc/hosts
exit
sudo cat /etc/hosts
kubens

sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
sudo virtualenv venv 
source venv/bin/activate
pip3 install -r requirements.txt

docker build -t welcome_image .
docker tag welcome_image k3d-mycluster-registry:5000/welcome_image:v0.1
docker push k3d-mycluster-registry:5000/welcome_image:v0.1
docker run -p 9091:9091 k3d-mycluster-registry:5000/welcome_image:v0.1
```

