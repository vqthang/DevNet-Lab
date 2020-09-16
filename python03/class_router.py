import pexpect

class NetworkDevice(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        return '--- Base Device, does not know how to get interfaces ---'


class NetworkDeviceIOS(NetworkDevice):

    # ---- Connect to device ----
    def connect(self):
        print('--- connecting IOS: telnet ' + self.ip_address)
        self.session = pexpect.spawn('telnet ' + self.ip_address, timeout=20)
        self.session.sendline('\r\n')
        result = self.session.expect(['Username:', pexpect.TIMEOUT])
        # Check for failure
        if result != 0:
            print('--- Timeout or unexpected reply from device')
            return None

        self.session.sendline(self.username)

        # Check network connection
        result = self.session.expect(['Password:', pexpect.TIMEOUT])
        if result != 0:
            print('--- Timeout or unexpected reply from device')
            return None

        # Successfully got password prompt, logging in with password
        self.session.sendline(self.password)
        self.session.expect('>')

    # ---- Get interfaces from device ----------------------------------
    def get_interfaces(self):
        self.connect()
        self.session.sendline('terminal length 0')
        self.session.expect('>')
        self.session.sendline('show interface')
        self.session.expect('>')
        return self.session.before

# Class to hold information about an IOS-XR network device

class NetworkDeviceXR(NetworkDevice):

    # Connect to device
    def connect(self):
        print('--- connecting XR: ssh ' + self.username + '@' + self.ip_address)
        # ---- Get interfaces from device ----------------------------------
    def get_interfaces(self):
        self.connect()
        return '--- XR Device interface info ---'
