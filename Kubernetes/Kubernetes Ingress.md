## Ingress
* 선행조건 : NodePort 를 지원하는 서비스 필요

### Ingress
* 하나의 IP 나 도메인으로 다수의 서비스를 제공 (L7)
* Ingress 생성하기
    ```
    # YAML
    apiVersion: extension/v1beta1
    kind: Ingress
    metadata:
      name: ingress
    spec:
      rules:
      - host: www.kei.com               # Domain 과 일치해야 함 
        http:
          paths:
          - path: /                     # 연결할 서비스 설정
            backend:
              serviceName: http-go-np
              servicePort: 8080
    ```
* Ingress 정보 확인하는 방법
    ```
    $ kubectl get ingresses
    ```

* 접속하는 방법

    * 접속을 위해 생성한 Ingress 내 Rule 과 일치해야 하므로 HTTP 요청의 Host 가 kei.com 값을 가질 수 있도록 hosts 파일을 변경해야 함
    ```
    $ sudo vi /etc/hosts
    ...
    < Ingress IP > www.kei.com
    ...

    # 테스트
    $ curl kei.com
    ```

* 다수의 서비스를 제공하는 방법
    ```
    # YAML
    apiVersion: extension/v1beta1
    kind: Ingress
    metadata:
      name: ingress
    spec:
      rules:
      - host: www.kei.com
        http:
          paths:
          - path: /
            backend:
              serviceName: http-go-np
              servicePort: 8080
      - host: dict.kei.com
        http:
          paths:
          - path: /
            backend:
              serviceName: http-go-np
              servicePort: 8080
      - host: map.kei.com
        http:
          paths:
          - path: /
            backend:
              serviceName: http-go-np
              servicePort: 8080

    # /etc/hosts 변경
    $ sudo vi /etc/hosts
    ...
    < Ingress IP >  www.kei.com dict.kei.com map.kei.com
    ...
    ```

* Ingress 로 HTTPS 서비스하는 방법

    * TLS 인증서 생성 
    ```
    $ openssl genrsa -out tls.key 2048
    $ openssl req -new -x509 -key tls.key -out tls.cert -days 360 -subj /CN=www.kei.com
    ```

    * TLS 인증서 등록
    ```
    $ kubectl create secret tls tls-secret  --cert=tls.cert --key=tls.key
    ```

    * 접속 확인
    
        * 옵션 -k : Allow Connections to SSL Site with certs
    ```
    $ curl -k www.kei.com
    ```
* Ingress 삭제하는 방법

    * Ingress 는 Ingress 지정을 통해 삭제가 가능하며 all 을 통해서는 삭제되지 않음
    ```
    $ kubectl delete ingress --all
    ```