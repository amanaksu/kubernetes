## Minikube

### 1. Install Docker
1. Install Docker
    ```
    $ sudo apt install docker.io -y
    ```

2. Docker 사용 권한을 변경한다. (Root -> User)
    ```
    $ sudo usermod -aG docker $USER && newgrp docker
    ```

3. docker 명령어로 Container 가 조회되는지 확인한다. 
    ```
    $ docker ps -a
    ```

### 2. Install Minikube
1. Install Minikube

    * Debian
    ```
    $ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
    $ sudo dpkg -i minikube_latest_amd64.deb
    ```

    * Ubuntu
    ```
    $  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    $ sudo install minikube-linux-amd64 /usr/local/bin/minikube
    ```

2. Start Minikube
    ```
    $ minikube start
    or 
    # docker driver is default.
    $ minikube start --driver=docker
    ```

### 3. (Optional) Install Kubectl
1. Install Kubectl CLI
    ```
    $ sudo snap install kubectl
    or
    $ sudo snap install kubectl --classic
    ```

### 4. Utility
1. Connect minikube on SSH 
    ```
    $ minikube ssh
    ```

### 5. Install Kafka on Minikube
1. Install minikube kafka cluster

    * Kafka Namespace : kafka-ca1
    ```
    $ git clone https://github.com/d1egoaz/minikube-kafka-cluster
    $ cd minikube-kafka-cluster
    $ kubectl apply -f 00-namespace/
    $ kubectl apply -f 01-zookeeper/
    $ kubectl apply -f 02-kafka/
    $ kubectl apply -f 03-yahoo-kafka-manager/
    ```

2. Run Kafka Manager

    * In Browser : < Minikube Cluster IP > : < Kafka-manager Service Port >
    ```
    $ kubectl get svc --namespace=kafka-ca1
    $ minikube ip
    ```

    * Add New Cluster for Cluster Zookeeper Hosts
    * Create Topic





## References
* [minikube 설치 방법](1)
* [Running Apache Kafka on Minikube](2)


[1]:https://blog.naver.com/isc0304/221879359568
[2]:https://technology.amis.nl/2019/03/24/running-apache-kafka-on-minikube/