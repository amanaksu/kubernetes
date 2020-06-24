## Storage
* Reference : [Volumes](1)

### Volume
* Container 가 External Storage 에 Access/Share 하는 방법
* Pod 의 각 Container 에 고유 분리된 File System 존재
* Volume 은 Pod 의 Component 이며 Pod 의 Spec 에 의해 정의됨
* 독립적인 Kubernetes Object 가 아니며 스스로 생성 / 삭제 불가
* 각 Container 의 File System 의 Volume 을 Mount 해 생성함

### Volume 유형
* Temporary Volume : emptyDir

    * Container 간 데이터 공유 목적
    * Container 종료(파괴) 시 삭제됨

* Local (Node) Volume : hostpath, local

    * Node 와 데이터 공유 목적
    * Pod 가 실행되는 Node 내 File System 공유 (like 공유 폴더)
    * Pod 가 실행되는 Node 가 변경되면 Data 가 변경됨

* Network Volume : iSCSI, NFS, cephFS, glusterFS ...

    * Cluster 외부에 있는 Resource 와 데이터 공유 목적

* Network Volume (only Cloud) : gcePersistentDis, awsEBS, azureFile ...

### 주요 사용 가능한 Volume 유형
* emptyDir : 일시적인 데이터 저장, 비어있은 디렉터리
* hostPath : Pod 에 Host Node 의 파일 시스템에서 파일이나 디렉터리를 마운트
* nfs : 기존 NFS ( Network File System ) 공유가 Pod 에 장착
* gcePersistentDisk : 구글 컴퓨트 엔진 (GCE) 영구 디스크 마운트
* persistentVolumeClaim : 사용자가 특정 클라우드 환경의 세부 사항을 모른채 GCE PersistentDisk 또는 iSCSI Volume 과 같은 내구성 Storage 를 요구(Claim) 할 수 있는 방법
* configMap, Secret, downwardAPI : 특수한 유형의 Volume





[1]:https://kubernetes.io/docs/concepts/storage/volumes/