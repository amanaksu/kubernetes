## Kubernetes Replication Control or Replica

### 1. ReplicationControl
* Pod가 항상 실행되도록 유지하는 Kubernetes Resource
* Default Wait Time : 5min
* 요소

    * Label Selector : Replication Controller 가 관리하는 Pod 범위 결정
    * 복제본 수 : 실행해야 하는 Pod 수
    * Pod Template : 새로운 Pod 형태

* 장점

    * Pod 가 없는 경우, 새 Pod 를 항상 실행
    * Node 장애 발생시 다른 Node 에 복제본 생성
    * 수동 / 자동으로 수평 스케일링

* 정책을 적용하는 방법 (ex: scale)

    * Command : kubectl scale rc < Name > --replicas= < Replica Num >
    ```
    $ kubectl scale rc http-go --replicas=5
    ```
    * YAML 수정 (defautl Edit: vim)
    ```
    $ kubectl edit rc http-go
    ```
    * YAML 업데이트
    ```
    $ cp http-go-rc.yaml http-go-rc-v2.yaml
    # http-go-rv-v2.yaml 수정
    $ kubectl apply -f http-go-rc-v2.yaml
    ```