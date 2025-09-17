import paramiko
import re

def ssh_command(host, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password, look_for_keys=False)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output

def parse_interfaces(show_interface_output):
    interfaces = []
    for line in show_interface_output.splitlines():
        # Match interface lines like "GigabitEthernet0/0" at the start
        match = re.match(r'^(GigabitEthernet\d+/\d+)', line.strip())
        if match:
            iface = match.group(1)
            interfaces.append(iface)
    return interfaces
