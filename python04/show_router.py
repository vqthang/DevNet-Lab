from netmiko import ConnectHandler

router_info = {
    'device_type': 'juniper',
    'host':   '36.37.255.1',
    'username': 'thangvq1',
    'password': '***',
    'port' : 22
}

def make_connect(router):
    net_connect = ConnectHandler(**router)
    return net_connect

if __name__ == "__main__":
    net_connect = make_connect(router_info)
    net_connect.enable()
    output = net_connect.send_command('show interfaces descriptions')
    print(output)
