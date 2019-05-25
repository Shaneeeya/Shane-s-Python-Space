import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port =int(input("请输入对方的port:"))


    # 从键盘获取数据
    send_data  = input("清输入要发送的数据:")

    # 可以使用套接字收发数据
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip ,dest_port))
    
    # 关闭套接字
    udp_socket.close()
    print("run")
if __name__ == "__main__":
	main()
