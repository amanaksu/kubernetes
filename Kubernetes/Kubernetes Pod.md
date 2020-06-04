## Pod

### 1. Properties
* Pod 내 모든 Container는 동일한 네트워크, 동일한 IPC Namespace, UTS Namespace 에서 실행
* Host Name 과 Network Interface 공유 -> Port 충돌 이슈 
* Pod 내 모든 Container는 IPC 를 통해 통신 가능 

### 2. Definition Pod on YAML
* apiVersion : Kubernetes API Version
* kind : Resource Type (ex: Pod ReplicaController, Service ..)
* Metadata : Pod Name, Namespace, Label, etc
* Spec : Container, Volume 
* Status (writer : Kubernetes) : Pod Status, Container Description, Pod IP, etc 

### 3. Create Pod by YAML
* Reference Image Path : https://hub.docker.com
* create YAML file
    ```
    apiVersion: v1
    kind: Pod
    metadata:
        name: http-go
    spec:
        containers:
        - name: http-go
          image: amanaksu/http-go
          ports:
          - containerPort: 8080
    ```
* create Pod by YAML
    ```
    $ kubectl create -f http-go-pod.yaml
    ```
* annotation on Pod
    ```
    $ kubectl annotate pod http-go test=1234
    (check) > kubectl get pod -o yaml
    ```
* delete Pod 
    ```
    $ kubectl delete -f http-go-pod.yaml
    ```
    or
    ```
    $ kubectl delete pod http-go
    ```
    or
    ```
    # delete all pods
    $ kubectl delete pod --all
    ```

### 4. [Probe][4]
* Liveness Probe  = is Live  or restart

    * 컨테이너가 살아있는지 판단하고 다시 시작함

* Readiness Probe = is Ready or Not LoadBalancing

    * Pod 준비상태인지 확인하고 적절하지 않는 경우 로드밸런싱을 하지 않음

* Startup Probe
    
    * Application 이 시작될 때까지 기다리며, Liveness Probe / Readiness Probe 기능을 비활성화함






### 99. Reference
* [YAML 생성 참조][1]
* [Kubectl Cheatsheet][2]
* [Pod Overview][3]
* Reference Command
    ```
    $ kubectl explain pods
    ```

[1]:https://kubernetes.io/docs/reference/
[2]:https://kubernetes.io/docs/reference/kubectl/cheatsheet/
[3]:https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/
[4]:https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/