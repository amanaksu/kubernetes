# test_server.py
import socket

with socket.socket() as s:
    s.bind(("0.0.0.0", 12345))
    s.listen()
    print("[+] server is started")

    conn, addr = s.accept()
    # conn : Client 와 통신할 소켓
    # addr : Client 의 정보가 들어있음
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break

            conn.sendall(data)