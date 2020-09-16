import pexpect

router = {'name': 'R4',
          'ip': '10.0.137.69',
          'username': 'cisco',
          'password': 'cisco'}


def connect(router_ip, router_user, router_pw):
    """
    Make a connection to Router
    :param router_ip: the ip of router
    :param router_user: the user of router
    :param router_pw: the password of router
    :return: session
    """
    print('You are using function to connecting to PNETlab', router_ip)
    session = pexpect.spawn('telnet ' + router_ip, timeout=20)
    session.sendline('\r\n')
    result = session.expect(['Username:', pexpect.TIMEOUT])
    if result != 0:
        print('failure')
        return 0
    print('Connecting to PNETlab : username: ' + router_user)
    session.sendline(router_user)

    result = session.expect(['Password:', pexpect.TIMEOUT])
    if result != 0:
        print('failure')
        return 0
    print('connecting to PNETlab : Password: ' + router_pw)
    session.sendline(router_pw)
    session.expect('>')
    return session


def get_router_info(session):
    session.sendline('terminal length 0')
    session.expect('>')
    session.sendline('show interface summary')
    session.expect('>')
    output = session.before
    return output


# make a function to print the device info
def print_device_info(device_info, show_int_output):
    print('PNETdevice Name: {0}'.format(device_info['name']))
    print('PNETdevice IP: {0}'.format(device_info['ip']))
    print('PNETdevice Username: {0}'.format(device_info['username']))
    print('PNETdevice Password: {0}'.format(device_info['password']))
    print('-------------')
    print('Show interface output --- inventory')
    print(show_int_output)


if __name__ == '__main__':
    session = connect(router['ip'], router['username'], router['password'])
    if session == 0:
        print('Tellneting to PNETlab devices failed')
    show_int_ouput = get_router_info(session)
    print_device_info(router, show_int_ouput)
    session.sendline('quit')
    session.kill(0)
