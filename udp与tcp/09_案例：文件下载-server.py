import socket

def send_file_2_client(new_client_socket, client_addr):
    # 接收客户端发送过来的要下载的文件名
    file_name = new_client_socket.recv(1024).decode("gbk")
    print("客户端(%s)需要下载的文件是:%s" % (str(client_addr), file_name))
    
    file_name = None
    # 打开文件读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)
    if file_name:
        new_client_socket.send(file_content)



def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:   
        new_client_socket, client_addr = tcp_server_socket.accept()
        
        # 调用发送文件函数
        send_file_2_client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
