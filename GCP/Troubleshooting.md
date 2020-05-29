### 1. when expose deployment, error comment "deployment.extensions" in Google Cloud Shell
* Command
```
kubectl run nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=LoadBalancer
```
* Error
```
Error from server (NotFound): deployments.extensions "nginx" not found
```
* Resolved
```
kubectl expose pod nginx --port=80 --type=LoadBalancer
```