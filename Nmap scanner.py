# para instalar packages do nmap "pip install python-nmap"
import nmap

nm = nmap.PortScanner()

target = "IP"

nm.scan(target, arguments='-sV -sC')

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))

