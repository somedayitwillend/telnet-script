import getpass
import telnetlib


# use the routers ip 
target = "192.168.8.1"
user = input("Enter telnet user: ")
passwd = getpass.getpass()

tnet = telnetlib.Telnet(target)

tnet.read_until(b"Username: ")
tnet.write(user.encode('ascii') + b"\n")

if passwd:
    tnet.read_until(b"Password: ")
    tnet.write(passwd.encode('ascii') + b"\n")

# write your cisco ios commands in between the quotation marks before the \n

tnet.write(b"ena\n")
tnet.write(b"cisco\n")
tnet.write(b"conf t\n")
tnet.write(b"int loop 0\n")
tnet.write(b"ip add 1.1.1.1 255.255.255.255\n")
tnet.write(b"no sh\n")
tnet.write(b"end\n")
tnet.write(b"exit\n")

print(tnet.read_all().decode('ascii'))
