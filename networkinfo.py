networks = {}
more = 'YES'
yesnoAns = ['Y','YE','YES','N','NO']
yesAns = ['Y','YE','YES']
noAns = ['N','NO']
while more in yesAns :
    vlan = input('What is the vlan ID?: ')
    while int(vlan) < 0 or int(vlan) > 4096:
        vlan = input('What is the vlan ID?: ')
    vlanName = input('What is the name for vlan ' + str(vlan) + '?: ')
    vlanNetwork = input('What is the network for vlan ' + str(vlan) + '?: ')
    vlanMask = input('What is the network mask for vlan ' + str(vlan) + '?: ')
    vlanGateway = input('What is the default gateway for vlan ' + str(vlan) + '?: ')
    networks[vlan] = vlan
    networks[vlan] = {}
    networks[vlan]['vlanName'] = vlanName
    networks[vlan]['vlanNetwork'] = vlanNetwork
    networks[vlan]['vlanMask'] = vlanMask
    networks[vlan]['vlanGateway'] = vlanGateway
    more = input('Are there any more VLANs(YES/NO)?: ').upper()
    while more not in yesnoAns:
        more = input('Are there any more VLANs(YES/NO)?: ').upper()
for net in networks:
    print('vlan ' + net)
    print('  name ' + networks[net]['vlanName'])
managementVlan = input('What is the switch management vlan?: ')
if managementVlan not in networks:
    print('Did you forget to add the vlan!?')

managementIP = input('What is the management IP?: ')
print('interface vlan ' + managementVlan)
print('  ip address ' + managementIP + ' ' + networks[managementVlan]['vlanMask'])
