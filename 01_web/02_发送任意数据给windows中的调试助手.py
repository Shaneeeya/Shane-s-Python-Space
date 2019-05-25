import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    send_data  = input("清输入要发送的数据:")
    # 可以使用套接字收发数据
    udp_socket.sendto(send_data.encode("gbk"), ("192.168.159.1",8080))
    
    # 关闭套接字
    udp_socket.close()
    print("run")
if __name__ == "__main__":
	main()
