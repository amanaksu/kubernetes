## Kubernetes App by GO

### 1. Create App by GO
1. create go program
    * Path : ./First GO App/main.go
2. build go program
    * Install Requirements
    ```
    $ apt install golang
    $ go get github.com/julienschmidt/httprouter
    ```
    * File Name : main.go
    ```
    $ go build main.go
    > main
    ```
3. create dockerfile
    * Path : ./First GO App/dockerfile
    * Build dockerfile
    ```
    $ docker build -t http-go .
    ```
4. Test
    ```
    $ docker run -d --rm -p 8080:8080 http-go
5. Push on Docker Hub
    ```
    $ docker tag http-go amanaksu/http-go
    $ docker login
    $ docker push amanaksu/http-go
    ```

### 2. Execute App on Kubernetes
1. Test
    ```
    # kubectl version < 1.18
    $ kubectl run http-go --image=amanaksu/http-go --port=8080

    # kubectl version >= 1.18
    $ kubectl create deploy http-go --image=amanaksu/http-go
    ```

2. Expose Service
    * "Pods Name" is found using command "kubectl get pods"
    * "LoadBalancer" is assigned an external IP.
    ```
    $ kubectl expose pods http-go-76c9445b75-z85qf --name=http-go-svc --type=LoadBalancer --port=8080
    ```