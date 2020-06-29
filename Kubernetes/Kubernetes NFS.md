## NFS

### 1. Install NFS Volume
* Install NFS Server
    ```
    $ apt-get update
    $ apt-get install nfs-common nfs-kernel-server postmap
    ```

* Change Share Directory Permission
    ```
    $ mkdir /home/nfs   # Share Directory
    $ chmod 777 /home/nfs
    ```

* Modify Configure : /etc/exports
    ```
    # Seperate "Space"
    # < Share Directory >   < Allow IP > (rw,sync,no_subtree_check) < Allow IP > ~~~

    /home/nfs 192.168.174.130(rw,sync,no_subtree_check) 192.168.174.133(rw,sync,no_subtree_check) 192.168.174.134(rw,sync,no_subtree_check) 
    ```

* NFS Server Restart
    ```
    $ sudo service nfs-server restart
    ```

* Check Mountable Space
    ```
    $ showmount -e 127.0.0.1
    ```

* Mount Share Directory

    * mount -t nfs < NFS Server IP >:< Share Directory Path > < Mounted Path >
    ```
    $ sudo mount -t nfs 192.168.174.134:/home/nfs /mnt
    ```
