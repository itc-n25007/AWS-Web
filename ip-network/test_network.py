from calc_network import calc_network_address

# テスト1
ip = "192.168.1.10"
mask = "255.255.255.0"

result = calc_network_address(ip, mask)

print("IPアドレス :", ip)
print("ネットマスク :", mask)
print("ネットワークアドレス :", result)

# テスト2
ip2 = "10.0.5.25"
mask2 = "255.255.0.0"

result2 = calc_network_address(ip2, mask2)

print("IPアドレス :", ip2)
print("ネットマスク :", mask2)
print("ネットワークアドレス :", result2)
