## Docker Private Registry

### 1. Create Docker Private Registry
```
sudo docker run -d --name docker-registry -p 5000:5000 registry
```

### 2. PUSH Docker Image in Docker Private Registry
* sudo docker tag < Tag Name > < Private Registry Address > / < Tag Name >
* sudo docker push < Private Registry Address > / < Tag Name >
```
sudo docker tag echo 127.0.0.1:5000/echo
sudo docker push 127.0.0.1:5000/echo
```

### Reference
* Auth : https://docs.docker.com/registry/configuration/#auth