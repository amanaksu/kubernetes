## Docker Commands

### 1. Docker Image Download & Delete (example: tomcat-7.0)
* Download :: sudo docker pull < Image Name >
```
sudo docker pull consol/tomcat-7.0
```
* Delete :: sudo docker rmi < Image Name >
```
sudo docker rmi consol/tomcat-7.0
```

### 2. List Docker Images
```
sudo docker images
```

### 3. Create Container (example: tomcat-7.0)
* sudo docker create < Image Name >
```
sudo docker create consol/tomcat-7.0
```

### 4. Run Container (example: tomcat-7.0)
* sudo docker run [ Options ] < Image Name >
```
sudo docker run -d --name tc consol/tomcat-7.0
```

### 5. List Container just runtime container
```
sudo docker ps
```
or
```
sudo docker container ls
```

### 6. List Container ALL include Stop Container
```
sudo docker ps -a
```
or
```
sudo docker container ls -a
```

### 7. Stop Container (example: tomcat-7.0)
* sudo docker stop < Container ID | Container Name >
```
sudo docker stop consol/tomcat-7.0:latest
```

### 8. Delete Container (must be Stopped Container)
* sudo docker rm < Container ID | Container Name >
```
sudo docker rm consol/tomcat-7.0:latest
```


---
## Command Expansion

### 1. Run Docker Image using Port forwarding (example: tomcat-7.0)
```
sudo docker run -d --name tc -p 80:8080 tomcat-7.0
```

### 2. Execute Shell on Container
```
sudo docker exec -it /bin/bash
```

### 3. Check Container logs
```
sudo docker logs tc #stdout, stderr
```

### 4. Copy From Host to Container
```
sudo docker cp < From Local Path > < to Container Name > : < inside Container Path >
sudo docker cp < From Container Name > : < inside Container Path > < To Local Path >
sudo docker cp < From Container Name > : < inside Container Path > < To Container Name > : < inside Container Path >
```

### 5. Create Temporary Container (example: tomcat-7.0)
```
sudo docker run -d -p 80:8080 --rm --name tc tomcat-7.0
```