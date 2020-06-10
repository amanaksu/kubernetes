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

### 3. Rolling Update
* 새 버전을 실행하는 동안 구 버전 Pod 와 연결
* Load Balancer 가 Pod 에 Job 을 할당할 때 Label 을 기반으로 동작하므로 서비스 Label 을 수정해 서비스 Pod 를 변경할 수 있음
* 하위 호환을 지원해야 함    

* Image Update 하는 방법
    ```
    $ kubectl set image deployment http-go http-go=gasbugs/http-go:v2
    ```
* 이전 버전으로 RollBack 하는 방법
    ```
    $ kubectl rollout undo deployment http-go
    ```
* 특정 버전으로 RollBack 하는 방법
    ```
    $ kubectl rollout undo deployment http-go --to-revision=1
    ```
* Rolling Update 를 일시 중지하는 방법
    ```
    $ kubectl rollout pause deployment http-go
    ```
* Rolling Update 일시 중지를 취소하는 방법
    ```
    $ kubectl rollout undo deployment http-go
    ```
* Rolling Update 를 재시작하는 방법
    ```
    $ kubectl rollout resume deployment http-go
    ```
* Deployment 과정의 이력 (명령어 History) 를 기록하는 방법
    ```
    $ kubectl create -f http-go-deployment.yaml --record=true
    ```
* Deployment 과정의 업데이트 이력 확인하는 방법 (ReplicaSet Max : 10)
* Rollback 을 해도 History 의 리비전은 유지됨
    ```
    $ kubectl rollout history deployment http-go
    ```
* Deployment 상태 확인하는 방법
    ```
    $ kubectl rollout status deployment http-go
    ```
* Deployment 속도 조정하는 방법
    ```
    $ kubectl path deployment http-go -p '{"spec": {"minReadySeconds": 10}}'
    ```
* Deployment 모니터링하는 프로그램 실행
    ```
    $ while true; curl < ip >; sleep 1; done
    ```

### 4. Cases that fail to Rolling Update
1) 할당된 리소스가 부족한 경우 (Insufficient quota)
2) Pod 가 준비되지 않은 경우 (Readiness probe failures)
3) 이미지가 없는 경우 (Image pull errors)
4) 권한 부족 (Insufficient permissions)
5) 제한 범위 초과 (Limit ranges)
6) 응용프로그램 실행 오류 (Application runtime misconfiguration)

* 업데이트 실패시 업데이트가 중지까지 소요 : 600초 (10분)