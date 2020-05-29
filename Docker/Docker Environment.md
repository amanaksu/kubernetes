## Using Docker Environment

### Set MySQL Service
1. Execute MySQL
* 환경 변수 "MYSQL_ROOT_PASSWORD" 명은 고정된 이름으로 변경해선 안된다. 
```
sudo docker run -d --rm --name mysql -e MYSQL_ROOT_PASSWORD='!qhdks00!' mysql
```

2. Check MySQL 
* 명령어 실행 후 'mysql>' 프롬프트 출력으로 정상적으로 실행됐음을 알 수 있다. 
```
sudo docker exec -it mysql mysql -u root -p
```

## FAQ
1. Error "event not found"
- Command 로 전달한 정보를 명령어로 인식한 경우 발생
- " 또는 ' 로 처리하면 됨