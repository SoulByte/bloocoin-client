import socket
import json
import addr

from server_data import ip, port


def register():
    if submit():
        print "Registration Success! Your bloocoin address is: " + addr.addr()
    else:
        print "Registration Failed"


def submit():
    reg = socket.socket()
    reg.connect((ip, port))
    reg.send(json.dumps({"cmd": "register"}))
    data = reg.recv(1024)
    if data:
        try:
            data = json.loads(data)
        except Exception, error:
            print error
            return False

        if data[u'success']:
            with open("bloostamp", 'wb') as file:
                file.write(data[u'payload'][u'addr'] + ":" + data[u'payload'][u'pwd'])
            return True
    else:
        return False
