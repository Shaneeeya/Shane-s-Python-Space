import socket
def main():
    # 1.买个手机（创建socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.插入手机卡（bind）
    tcp_server_socket.bind(("",7890))
    # 3.将手机设置为正常响铃模式
    tcp_server_socket.listen(128)
        
    while True:
        # 4.等待别人电话到来
        print("等待一个新的客户端的到来...")
        new_clinet_socket, client_addr = tcp_server_socket.accept()
        
        print("一个新的客户端已经到来%s" % str(client_addr))
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_clinet_socket.recv(1024)
            print("recv_data")
            print("客户端发送过来的请求是 %s" %recv_data.decode("gbk"))
            
            # 客户端发送空，意味着客户端关闭了
            if recv_data:
                # 回送一部分数据给客户端
                new_clinet_socket.send("哈哈哈哈哈哈哈".encode("gbk"))
            else:
                break

        # 关闭套接字
        new_clinet_socket.close()
        print("已经为这个客户端服务完毕")
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
