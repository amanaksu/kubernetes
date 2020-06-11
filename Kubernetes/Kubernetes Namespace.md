## Namespaces 

### 1. Namespaces
* 리소스를 분리된 영역으로 나누기 좋은 방법
* 쿠버네티스 시스템을 더 작은 그룹으로 분할
* 멀티 테넌트 환경을 분리하여 리소스를 생산, 개발, QA 환경 등으로 사용 가능
* 리소스 이름은 Namespaces 내에서만 고유 명칭 사용 

### 2. Command or YAML
* Namespaces 만드는 방법
    ```
    # YAML
    apiVersion: v1
    kind: Namespace
    metadata:
        name: test-ns
        ....
    ```
    or
    ```
    $ kubectl create namespace test-ns
    ```
* Namespaces 확인하는 방법
    ```
    $ kubectl get ns
    ```
* 전체 Namespaces 확인하는 방법
    ```
    $ kubectl get pod --all-namepsaces
    ```
* Namespaces 삭제하는 방법
    ```
    $ kubectl delete ns test-ns
    ```