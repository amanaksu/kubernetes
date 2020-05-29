## Kubernetes using GCP

### 1. sign up GCP
* sign up : [Google Cloud Platform][1]

### 2. Create Project
* (Optional) Change Region.

### 3. Test (example: nginx)
1. Inside Created Project
2. Create Cluster in "Cluster" Tab (2~3 min)
    - Not Change. Only Default Settings
3. Create nginx service    
    1) Connect to your cluster using Start Google Cloud Shell (click "connect" button)
    2) (if it is first connection) execute gcloud command on Google Cloud Shell (previous copy command)
    3) Set nginx
    ```
    kubectl run nginx --image=nginx
    ```
    4) Start nginx service
    ```
    kubectl expose deployment nginx --port=80 --type=LoadBalancer
    ```
    * Error : [Error from server (NotFound): deployments.extensions "nginx" not found][2]

    5) Check Started nginx service in "Service & Response" Tab



[1]:https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-KR-all-en-dr-bkws-all-all-trial-e-dr-1008074&utm_content=text-ad-none-none-DEV_c-CRE_255885830765-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+T1+%7C+EXA+%7C+General+%7C+M:1+%7C+KR+%7C+en+%7C+cloud+%7C+platform-KWID_43700020285731386-kwd-301388847745&userloc_1009856&utm_term=KW_gcp&gclid=CjwKCAjw5cL2BRASEiwAENqAPjRoE-VvY0wf_v_6jJGppeMqn_8QK1nnSZJxMVjuJRfphAdES-9fzBoCJ_gQAvD_BwE
[2]:./Troubleshooting.md