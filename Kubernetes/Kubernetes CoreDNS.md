## DNS

### DNS Service
* Service 를 생성하면, 대응되는 DNS Entry 가 생성
* DNS Entry : < Service Name >.< Namespace-Name >.svc.cluster.local
    ```
    $ curl http-go-svc.default.svc.cluster.local
    ```
    or
    ```
    $ curl http-go-svc.default
    ```
    or 
    ```
    $ curl http-go-svc
    ```

### CoreDNS
* 내부에서 DNS Server 역할을 하는 Pod
* 각 Middleware 를 통해 Logging, Cache, Kubernetes 를 질의하는 등의 기능 보유 
* configmap 저장소를 사용해 설정 파일을 제어
* Corefile 을 통해 현재 Cluster 의 NS 를 지정
* Pod 에서 Subdomain 을 사용하면 DNS Service 사용 가능

    * < HostName >.< SubDomain >.< Namespace>.svc.cluster-domain.example

       = < Pod Name >.< SubDomain >.< Namespace>.svc.cluster-domain.example
    ```
    # busybox-1.default-subdomain.default.svc.cluster-domain.example
    ```
    