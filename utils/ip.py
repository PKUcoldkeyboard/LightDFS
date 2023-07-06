import socket


def get_local_ip():
    try:
        # 创建一个连接到 Internet 的 socket
        # 参数中的 '8.8.8.8' 是 Google 的公共 DNS 服务器地址，'80' 是它的端口号
        # 我们并不真的需要连接到它，这只是为了获取本地 IP 地址
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    return ip
