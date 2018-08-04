from pexpect import pxssh 
import getpass

s=pxssh.pxssh()
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password:' )
s.login(hostname, username, password)
command = raw_input('enter a command: ')
s.sendline(command)
s.prompt()

