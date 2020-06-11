## Kubernetes Service

### 1. Pod 의 문제점
* Pod 는 외부에서 접근하기 위해 Port-Forward 나 Pod 내에서 외부와 통신하기 위한 별도의 서비스를 생성해야 함
* Pod 생성 / 삭제가 반복됨에 따라 IP 가 유동적이고, (Scaling 시) LoadBalancing 을 위한 개체가 필요

### 2. Service 의 요구사항
* 외부에서 Front-End Pod 로 연결해야 한다. 
* Front-End Pod 는 Back-End Pod 로 연결해야 한다. 
* Pod 의 IP 가 변경될 때마다 재설정하지 않아야 한다. 

### 3. Command & YAML
* Service 생성하는 방법
    ```
    $ kubectl expose ~~
    ```
    or
    ```
    # YAML
    apiVersion: v1
    kind: Service
    metadata:
        name: http-go-svc
    spec:
        ports:
        - port: 80
          targetPort: 8080
        selector:
          app: http-go
    ......
    ```
* Service 기능 확인하는 방법
    ```
    $ kubectl exec < Pod Name > --curl < Cluster IP >:8080 -s
    ```
* Service 의 Session 을 고정하는 방법

    * sessionAffinity 을 추가하면 최초 연결된 Pod 와 지속적으로 통신할 수 있도록 Session 을 유지시킴
    ```
    # YAML
    apiVersion: v1
    kind: Service
    metadata:
        name: http-go-svc
    spec:
        sessionAffinity: ClusterIP
        ports:
        - port: 80
          targetPort: 8080
        selector:
          app: http-go
    ......
    ```
* 다중 Port 에 Service 하는 방법 

    * spec.ports 하위에 열거하면 됨 
    ```
    .....
    spec:
        .....
        ports:
        - name: http
          port: 80
          targetPort: 8080
        - name: https
          port: 443
          targetPort: 8443
    .....
    ```
* Service 하는 IP 확인하는 방법
    ```
    $ kubectl describe svc http-go-svc
    ```
* 외부 IP 와 연결하는 방법

    * Service 와 Endpoints 리소스 모두 생성
    ```
    # external-svc.yaml
    apiVersion: v1
    kind: Service
    metadata:
        name: external-service
    spec:
        ports:
        - port: 80
    
    ---

    # external-endpoint.yaml
    apiVersion: v1
    kind: Endpoints
    metadata:
        name: external-service
    subsets:
        - addresses:
          - ip: 11.11.11.11
          - ip: 22.22.22.22
          ports:
          - port: 80
    ```