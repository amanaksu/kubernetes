## Kubernetes

### 장점
1. 애플리케이션 배포 단순화
2. 하드웨어 활용도 극대화
3. 상태 확인 및 자가 치유
4. 오토스케일링
5. 애플리케이션 개발 단순화

### 역할
* DevOps 가 원활히 이뤄질 수 있도록 개발자 / 운영자 지원
    - 핵심 애플리케이션 기능에 집중
      - 애플리케이션 개발자가 특정 인프라 관련 서비스를 애플리케이션에 구현하지 않아도 됨
      - 쿠버네티스에 의존해 서비스 제공
      - 애플리케이션 개발자는 애플리케이션의 실제 기능을 구현하는데 주력
      - 인프라와 인프라를 통합하는 방법을 파악하는데 낭비할 필요없음
    - 효과적으로 리소스 활용
      - 실행을 유지하고 서로 통신할 수 있도록 컴포넌트에 정보를 제공
      - 애플리케이션이 어떤 노드에서 실행되는지 상관없음
      - 언제든 애플리케이션을 재배치 가능
      - 애플리케이션을 혼합하고 매칭시킴으로써 리소스를 매칭


### 클러스터 아키텍쳐
1. 마스터 노드 ( Master Node ) : 전체 쿠버네티스 시스템을 **관리** 하고 통제하는 쿠버네티스 컨트롤 플레인을 관장
    - Kube-apiserver : 인증, 통신, 권한
    - Kube-Scheduler : 배치, 예약
    - Controller-Manager : 리소스 제어, 관리, YAML
    - etcd : DB

2. 워커 노드 ( Worker Node ) : 실제 배포하고자 하는 애플리케이션의 **실행**을 담당
    - Kubelet : 런타임 처리 (실제 실행), 컨테이너 관리
    - Kube-Proxy : 내부 컨테이너, 노드들의 통신

### 쿠버네티스에서 애플리케이션 실행
1. Docker Image 를 Docker Image Registry 에 PUSH 한다.
2. App Descriptor ( YAML or JSON ) 작성한다. 
3. Master Node 의 Control Plane 으로 전달한다. 
4. Control Plane 의 Kube-Apiserver 는 사용자를 인증/인가 후 Kubelet 에 전달한다. 
5. Kubelet 은 App Descriptor 에 맞춰 Docker Image 를 구성 후 실행한다. 