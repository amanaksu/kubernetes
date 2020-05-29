## How to build Docker Image for WordPress

### 1. pull xampp Docker Image
```
sudo docker pull xampp
```
or 
```
sudo docker run --name wp_blog -p 80:80 -d tomsik68/xampp 
```

### 2. Minimalize Docker Image
```
sudo docker exec -it wp_blog bash
```

* Change Owner
```
chown daemon. /opt/lampp/htdocs
```

* backup existed files & directory in web root directory
```
cd /opt/lampp/htdocs
mkdir backup
mv * ./backup/
exit
```

### 3. Setup WordPress in xampp
* Download WordPress in official site & unarchive
```
wget https://wordpress.org/latest.tar.gz
tar -xf latest.tar.gz
```

* Copy WordPress To Docker Images
```
sudo docker cp wordpress wp_blog:/opt/lampp/htdocs
``` 

* move to wordpress file path
```
sudo docker exec -it wp_blog bash
cd /opt/xampp/htdocs/wordpress
mv * ../
exit
```

* Connect 127.0.0.1/wp-admin using web browser

### 4. Build WordPress Blog in Docker Image
* must be stop docker image for Commit
```
sudo docker stop wp_blog
sudo docker commit wp_blog amanaksu/wp_blog
```

### 5. Upload to Docker Hub
```
sudo docker login
sudo docker push amanaksu/wp_blog
```