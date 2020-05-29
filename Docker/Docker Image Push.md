## Push Docker Image To Registry

### 1. Login Docker Site
* Site : hub.docker.com
```
sudo docker login
```

### 2. Change Docker Image Tag for PUSH on Docker Hub
* sudo docker tag < Before Tag Name > < New Tag Name >
```
sudo docker tag echo_test amanaksu/echo
```

### 3. PUSH Docker Image
```
sudo docker push amansksu/echo
```

### 4. Check History on Docker Image
* sudo docker history < Image Name >
```
sudo docker history mysql
```