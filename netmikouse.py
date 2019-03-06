from netmiko import ConnectHandler

#---------------Gather information---------------------
ip = input('What is the management IP?: ')
username = input('What is the username? [cisco]: ') or 'cisco'
password = input('What is the password? [cisco]: ') or 'cisco'

cisco_switch = {'device_type': 'cisco_ios',
                'ip': ip,
                'username': username,
                'password': password}

connection = ConnectHandler(**cisco_switch)

interface_output = connection.send_command('show ip interface brief')

#print(interface_output)
for line in interface_output:
    if 'up' in line:
        print(line)
print('--------adding AAA commands to the device ------')
commands = ['aaa authentication login default group radius local-case',
            'aaa authentication login vty group radius local-case',
            'aaa authorization exec default group radius local if-authenticated',
            'aaa accounting system default start-stop group radius',
            'ip radius source-interface Vlan1301',
            'radius-server host 192.168.1.10 auth-port 1645 acct-port 1646',
            'radius-server key cisco',
            'line vty 0 4',
            'login authentication vty']
configoutput = connection.config_mode()
if 'Invalid input' in configoutput:
    print(configoutput)
configoutput = connection.send_config_set(commands)
if 'Invalid input' in configoutput:
    print(configoutput)
print('------------------done------------------')
