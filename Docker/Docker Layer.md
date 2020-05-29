## Docker Layers

### 1. Chekc Docker Image Information (example: nginx)
* sudo docker insepct < Image Name >
```
sudo docker inspect nginx
```

### 2. Check Docker Image Repository
* Docker Image Repository on Local : /var/lib/docker/image
```
sudo docker info
```

### 3. Docker Layer Repository
* Local Repository : /var/lib/docker
* Docker 내 디렉터리를 Storage 로 별도 저장/마운트하기 위한 대상
```
/var/lib/docker
   > image
       > imagedb -> layerdb
       > layerdb -> overlay2
   > overlay2    -> l
       > l       => file system
```