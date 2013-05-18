import socket
import json
from server_data import ip, port


def transactions():
    with open("bloostamp", 'rb') as file:
        f = file.read().split(":")
        addr, pwd = f[0], f[1]
    s = socket.socket()
    s.connect((ip, port))
    s.settimeout(2)
    s.send(json.dumps({"cmd": "transactions", "addr": addr, "pwd": pwd}))
    data = ""
    while True:
        recv = s.recv(1024)
        if recv:
            data = data + recv
        else:
            break
    data = json.loads(data)
    try:
        for x in data['payload']['transactions']:
            if x['to'] == addr:
                print "From: "+x['from']+" "+str(x["amount"])
            if x['from'] == addr:
                print "To: "+x['to']+" "+str(x['amount'])
    except TypeError:
        print "You haven't made any transactions."
