import pexpect

host = "35.234.26.118 30001"
username = "cisco"
password = "cisco"
command = 'show ip int brief'

session = pexpect.spawn('telnet ' + host, timeout=20)

session.sendline('\r\n')

result = session.expect(['Username:', pexpect.TIMEOUT])
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])
session.sendline(password)
result = session.expect(['>', pexpect.TIMEOUT])
session.sendline('enable')
result = session.expect(['#', pexpect.TIMEOUT])
session.sendline(command)
result = session.expect(['#', pexpect.TIMEOUT])
session.close()
