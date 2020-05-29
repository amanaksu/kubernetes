## How to Set Jupyter Notebook with Volume Mount

### 1. File Sharing Using Volume Mount (example: nginx)
* docker run -v < Host Path > : < Container Path > : < Privilege >
```
sudo docker -d -p 80:80 --rm -v /var/www:/usr/share/nginx/html:ro nginx
```

### 2. Start JupyterLab with Volume Mount
* Privilege : rw
```
sudo docker --rm -p 8080:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work:rw jupyter/datascience-notebook:9b06df75e445
```