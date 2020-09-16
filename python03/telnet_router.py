from python03.class_router import NetworkDeviceIOS
from python03.class_router import NetworkDeviceXR

routers = [{'name': 'R4',
          'ip': '10.0.137.69',
          'username': 'cisco',
          'password': 'cisco',
          'os': 'IOS-XE'}]

def print_device_info(device, show_interface):
    print('-----------------------------------------------')
    print(' Device Name: ', device.name)
    print(' Device IP: ', device.ip_address)
    print(' Device username: ', device.username, end=' ')
    print(' Device password: ', device.password)
    print('')
    print('Interfaces')
    print('')
    print()
    print('------------------------------------------------\n\n')

if __name__ == '__main__':
    for router in routers:
        if router['os'] == 'IOS-XE':
            make_instance = NetworkDeviceIOS(name=router['name'],
                                             ip=router['ip'])
            interfaces = make_instance.get_interfaces()
            print_device_info(make_instance, interfaces)
        elif router['os'] == 'IOS-XR':
            make_instance = NetworkDeviceXR(name=router['name'],
                                            ip=router['ip'])
            interfaces = make_instance.get_interfaces()
            print_device_info(make_instance, interfaces)
