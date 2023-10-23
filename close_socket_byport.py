import psutil

def close_port(port_num):
    sockets = psutil.net_connections(kind='inet')

    for socket in sockets:
        if socket.laddr.port == port_num and socket.status == 'LISTEN':
            try:
                psutil.Process(socket.pid).terminate()
                print(f"the socket that listen on port {port_num} is closed .")
            except Exception as e:
                print(f"An error occur when close socket: {e}")



port_num = 5555  # Örnek olarak 8080 port numarasını kullanıyoruz
close_port(port_num)