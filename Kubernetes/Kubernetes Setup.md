## Setup Kubernetes Cluster

### 0. Pre-Infomation
* kubeadm : 클러스터를 부트스트랩하는 명령 ( 쿠버네티스 관리 명령 수행 )
* kubelet : 클러스터의 모든 시스템에서 실행되는 구성 요소로 창 및 컨테이너 시작 작업을 수행 (서비스)
* kubectl : 클러스터와 통신하는 사용자 클라이언트 프로그램

### 1. Install Kubernetes (Master Node)
* 설치명령들을 Shell Script 에 저장해서 실행하면 된다. 
```
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```
* Node 별 Hostname 을 다르게 설정한다. 
* sudo hoatname set-hostname < Host Name >
    - Master Node : master
    - Worker Node #1 : worker1
    - Worker Node #2 : worker2
```
sudo hostnamectl set-hostname master
```


### 2. Initialize Master Node (Master Node)
1) Master Node 초기화를 가장 먼저 수행
```
sudo kubeadm init
```

2) Swap 에러 발생시 Swap 기능 제거
```
sudo swapoff -a                                    # 현재 커널에서 Swap 기능 끄기
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab # Reboot 후에도 Swap 기능 유지
reboot                                             # 적용
                                                   # 재부팅 후
sudo kubeadm init                                  # 초기화 진행
```

- Kubernetes 에서 Swap 비활성화하는 이유
    - Kubernetes 1.8 이후 Node 에서 Swap을 비활성화해야 설치가 가능함 (or --fail-swap-on = false)
    - Kubernetes 아이디어는 인스턴스를 최대한 100% 에 가깝게 성능을 발휘하는 것
    - 모든 배포는 CPU / Memory 제한을 고정하는 것이 필요
    - 스케줄러가 Pod를 머신에 보내면 Swap 을 사용하지 않는 것이 필요
    - Swap 발생시 속도가 느려지는 이슈 발생
    - 성능을 위한 것


3) 초기화 성공시 결과 저장
* Client(kubectl) 을 위한 부분
```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

* Slave Node 가 Master Node 에 추가하기 위한 부분
```
kubeadm join 192.168.174.130:6443 --token geteqf.ianv3311d46qv747 \
    --discovery-token-ca-cert-hash sha256:1fb133ae4e834f702ba96b7c64910174b0f68d85ddc6eb0d700b1a523b0f5f12
```

### 3. Install Kubernetes (Slave Node)
* Master Node 의 Kubernetes 설치 방법과 동일 (위의 1번 항목)


### 4. Initalize Slave Node (Slave Node)
* Master Node 초기화 성공시 출력된 Slave Node 가 Master Node 에 추가되기 위한 명령 사용


### 5. Check Node Status
```
kubectl get node
```
* 현재 모든 Node 의 STATUS 가 "NotReady" 임을 알 수 있다. >  Network 설정 필요

### 6. Pod Network 추가 (Master Node)
* Kubernetes 에서는 다양한 종류의 3rd Network 를 지원함
```
# Calido
kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml

# Cilium
kubectl create -f https://raw.githubusercontent.com/cilium/cilium/v1.6/install/kubernetes/quick-install.yaml

# Weave Net
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```
* Contiv-VPP : [매뉴얼 참고](4)
* Kube-Route : [매뉴얼 참고](5)

### 7. Check Node Status
```
kubectl get node
```
* 모든 Node 의 STATUS 가 "Ready" 임을 알 수 있다. 

### 8. Test : Kubernetes 에 Docker Image 올리기 (example: nginx)
1) Pod 생성
* nginx Docker Image 가 Local 에 없으면 Docker Hub 에서 가져옮
```
kubectl run nginx --image=nginx
```

2) 생성된 Pod 확인
```
kubectl get pod
```

3) nginx 포트 포워딩
```
kubectl port-forward nginx 8080:80
```

4) 브라우저로 nginx 접속 (127.0.0.1:8080)


### 98. Troubleshooting
* kubeadm init or join 명령을 실행할 때 중복된 실행으로 문제가 발생하는 경우
```
kubeadm reset       # 초기화
```



### 99. Reference
* [Why disable swap on kubernetes](1)
* [Install Kubeadm](2)
* [Create Cluster Kubeadm](3)

[1]: https://serverfault.com/question/881517/why-disable-swap-on-kubernetes
[2]: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
[3]: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
[4]: https://github.com/contiv/vpp/blob/master/docs/setup/MANUAL_INSTALL.md
[5]: https://github.com/cloudnativelabs/kube-router/blob/master/docs/kubeadm.md