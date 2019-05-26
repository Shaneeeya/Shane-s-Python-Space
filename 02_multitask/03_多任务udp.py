import socket
import threading

def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """接收数据"""
    """发送数据"""
    while True:
        send_data = input("输入要发送的信息：")
        udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

def main():
    """udp聊天器"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 1024))
    
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))
    # 创建两个线程，执行相应的功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()
