import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localddr = ("", 7788)
    udp_socket.bind(localddr)
    # 3.接受数据
    
    recv_data = udp_socket.recvfrom(1024)
    # recv_data 这个变量中储存的是一个元组（接收到的数据（发送方的ip，port））
    recv_msg = recv_data[0]
    send_addr = recv_data[1]
    # 4.打印接收到的数据
    print("%s: %s", (str(send_addr), recv_msg.decode("gbk")))

    # 5.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
