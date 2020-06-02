## Docker Container 실행 연습문제

### 1. 실행/저장된 모든 Docker Image 를 삭제하기
    ```
    sudo docker stop `sudo docker ps -a -q`
    sudo docker rm `sudo docker ps -a -q`
    ```
    or
    ```
    sudo docker rmi `sudo docker images -q`
    ```

### 2. Docker 기능을 사용해 Jenkins 검색하기
    ```
    sudo docker search jenkins
    ```

### 3. Jenkins 를 사용하여 설치하기
    ```
    sudo docker pull jenkins
    sudo docker inspect jenkins
    sudo docker run -d -p 8080:8080 --name jenkins jenkins
    ```
    
### 4. Jenkins 포트로 접속하여 웹 서비스 열기
    ```
    < web brwoser > 127.0.0.1:8080
    ```

### 5. Jenkins 의 초기 패시워드를 찾아서 로그인하기 
    ```
    sudo docker exec -it jenkinse cat /path/initPassword
    ```
    or 
    ```
    sudo docker logs jenkins
    ```
