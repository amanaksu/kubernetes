## StatefulSet
* Application 의 상태를 저장하고 관리하는데 사용되는 객체 

### Use Case
1. 안정적이고 고유한 네트워크 식별자가 필요한 경우
2. 안정적이고 지속적인 Storage를 사용해야 하는 경우 
3. 질서 정연한 Pod 의 배치와 확장을 원하는 경우
4. Pod 의 Auto Rolling Update 를 사용하기 원하는 경우

### Problems to be solved
1. Statefulset 과 관련된 Volume이 삭제되지 않음 (관리필요)
2. Pod 의 Storage 는 PV 나 StorageClass 로 Provisioning 해야함
3. Rolling Update 를 수행하는 경우 수동으로 복구해야 할 수 있음 (Rolling Update 수행시 기존 Storage 와 충돌로 인해 Application 이 오류가 발생할 수 있음)
4. Pod Network ID 를 유지하기 위해 Headless Service 필요

### Update
1. OnDelete

    - Pod 를 자동으로 Update 하는 기능이 아님
    - 수동으로 삭제하면 StatefulSet 의 spec.template 를 적용한 새로운 Pod 가 생성됨
2. RollingUpdate

    - RollingUpdate 를 구현하면 한번에 하나씩 Pod 를 Update 함
    - Pod 역순으로 진행