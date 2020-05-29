## Docker Build using dockerfile

### 1. Create dockerfile
* 파일명은 "dockerfile" 로 고정된 이름을 사용함

### 2. Build Image
* sudo docker budil -t < Tag Name > < dockerfile Path >
```
sudo docker build -t echo_test .
```

### 3. Start Docker Image
* 정상 연결을 확인하기 위해 -t (Termianl) 옵션을 부여함
```
sudo docker run --rm -t -p 12345:12345 --name echo echo_test
```