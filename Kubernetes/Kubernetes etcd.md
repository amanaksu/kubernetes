## Inside etcd 

### 1. Install opensource etcd-io for client interface
* Download etcd-io by wget & Extract files
    ```
    $ wget https://github.com/etcd-io/etcd/releases/download/v3.4.9/etcd-v3.4.9-linux-amd64.tar.gz
    $ tar -xvf etcd-v3.4.9-linux-amd64.tar.gz
    ```

### 2. print data inside etcd
* connect etcd on kubernetes by etcdctl in etcd-io (SSL)

    - ETCDCTL_API=3 : set api version in environment

    - endpoints < IP:Port > : etcd server ip
        > sudo cat /etc/kubernetes/manifests/kube-apiserver.yaml

    - ca : /etc/kubernetes/pki/etcd/ca.crt

    - cert : /etc/kubernetes/pki/etcd/server.crt

    - key : /etc/kubernetes/pki/etcd/server.key

    ```
    $ sudo ETCDCTL_API=3 ./etcdctl --endpoints 127.0.0.1:2379 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt --key /etc/kubernetes//pki/etcd/server.key get / --prefix --keys-only
    ```