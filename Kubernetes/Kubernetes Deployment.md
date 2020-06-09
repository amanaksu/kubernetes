## Deployment 

### 1. Deployment
* 다수의 ReplicaSet 을 다룰 수 있는 상위 객체 
* Application (or ReplicaSet) 을 다운타임없이 업데이트 가능하도록 도와주는 리소스
* 모든 Pod 를 업데이트하는 방법

    * Re-Create : 새로운 Pod를 실행시키고 작업이 완료되면 오래된 Pod 를 삭제하는 방식, 잠깐 다운타임 발생
    * Rolling : 낮은 버전의 Pod 를 하나씩 교체하면서 업데이트하는 방식

### 2. Deployment Scaling
* ReplicationControl or ReplicaSet 의 Scaling 방식과 동일함 
    ```
    $ kubectl scale deploy < Deploy Name > --replicas=<Number>
    or
    $ kubectl edit deploy < Deploy Name >
    ```