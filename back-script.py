import netmiko
from netmiko import ConnectHandler

mikrotik_router_1 = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.88.1',
    'port': '22',
    'username': 'admin+ct',
    'password': 'cisco'
}

sshCli = ConnectHandler(**mikrotik_router_1)

output = sshCli.send_command("/interface ethernet print")
print(output)

command = "/export"
output = sshCli.send_command(command)
print(output)

file = open("BackUp-Config-Mikrotik-Netmiko.txt", "w")
file.write(output)
file.close()

sshCli.disconnect()