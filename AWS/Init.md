## Kubernetes using AWS

### 1. sign up AWS
* sign up : [AWS][1]

### 2.1. Start EKS with eksctl
* kubectl command line utility
1. Authentication
    ```
    $ sudo apt install awscli
    $ aws configure
    > AWS Access Key ID [None]: < Input >
    > AWS Secret Access Key [None]: < Input >
    Default region name [None]: ap-northeast-2 (korea region)
    Default output format [None]: json
    ```
2. Install eksctl
    ```
    $ curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
    $ sudo mv /tmp/eksctl /usr/local/bin
    $ eksctl version
    ```
    * Error : [cannot found kubectl][2]

### 2.2. Start EKS with AWS Management
* using AWS Management Console

### 3. Create Cluster
```
$ eksctl create cluster --name prod --version 1.12 --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --node-ami auto
```

### 4. 



[1]:https://aws.amazon.com/ko/console
[2]:./Troubleshooting.md