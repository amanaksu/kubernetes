## What can be done in Service on Kubernetes

### 1. Deploying scaling
* kubectl scale deploy < Pods Name > --replicas=< Scale-out Number >
* "Scale-out Number" is Total Number, NOT Number of nodes to be expanded
    ```
    $ kubectl scale deploy http-go --replicas=3
    ```

### 2. View more information
* Describe Pod Info : kubectl describe pod < Pod Name >
    ```
    $ kubectl describe pod http-go-76c9445b75-mb5qd 
    ```
* Checking the node where pods are deployed
    ```
    $ kubectl get pods -o wide
    ```