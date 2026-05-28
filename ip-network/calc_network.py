import socket
import struct

def calc_network_address(ip_addr, netmask):
    # IPアドレスを整数へ変換
    ip = struct.unpack("!I", socket.inet_aton(ip_addr))[0]

    # ネットマスクを整数へ変換
    mask = struct.unpack("!I", socket.inet_aton(netmask))[0]

    # AND演算
    network = ip & mask

    # IPアドレス形式へ戻す
    return socket.inet_ntoa(struct.pack("!I", network))
