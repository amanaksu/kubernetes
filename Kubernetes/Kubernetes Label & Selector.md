## Label (like tag) & Selector
* "Key : Value" 데이터로 리소스를 필터링시 사용

    * app : 어플리케이션 구성요소, 유형
    * rel : 어플리케이션 버전 지정 

* YAML 내 지정 위치
    ```
    apiVersion: v1
    kind: Pod
    metadata:
        name: nodejs-manual-v2
        labels:
            creation_method: manual
            evn: prod
    .....
    ```
* 기존 Pod 내 Label 을 추가하는 방법

    * kubectl label pod < Pod Name > < Label's Key = Value >
    ```
    $ kubectl label pod http-go-v2 test=foo
    ```
* 기존 Pod 내 Label 을 수정하는 방법

    *kubectl label pod < Pod Name > < Label's Key = Value > --overwrite
    ```
    $ kubectl label pod http-go-v2 test=foo2 --overwrite
    ```
* 기존 Pod 내 Label 을 확인하는 방법
    ```
    $ kubectl get pod --show-labels
    ```
* 기존 Pod 내 Label 을 검색하는 방법
    ```
    # 특정 컬럼 (Key) 가 "env" 인 것만 출력
    $ kubectl get pod --show-labels -l "env"

    # 특정 컬럼 (Key) 가 env 인 것만 출력
    $ kubectl get pod --show-labels -l "!env"

    # 특정 컬럼 (Key) 의 Value 가 test 가 아닌 것만 출력
    $ kubectl get pod --show-labels -l "env != test"

    # 특정 컬럼 (Key) 의 Value 가 test 가 아니고, rel 은 test 인 것만 출력
    $ kubectl get pod --show-labels -l "env != test, rel=beta"
    ```
* 기존 Pod 내 Label 을 특정 컬럼 (Key) 만 확인하는 방법

    * kubectl get pod -L < 특정 컬럼 (Key) >
    ```
    $ kubectl get pod -L test
    ```
* 기존 Pod 내 Label 을 삭제하는 방법

    * kubectl label pod < Pod Name > < Label's Key> -
    ```
    $ kubectl label pod http-go-v2 test-
    ```
* [Label 배치 전략][1]


[1]:https://www.replex.io/blog/9-best-practices-and-examples-for-working-with-kubernetes-labels