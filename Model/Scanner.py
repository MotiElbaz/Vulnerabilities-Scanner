from threading import Lock
import nmap as nmap
import urllib.request
import Objects.Node as Node
import Objects.Vulnerability as Vulnerability
import Objects.Reachability as Reachability
import Model.DAL as DAL
import Model.ReasoningEngine as ReasoningEngine
import logging

logging.basicConfig(filename='LOG.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Scanner(object):
    _instance = None

    def scan(self, subnets):
        """
        Scanning the lan topology.
        """
        Node.idGenerator = 0
        dal = DAL.DAL()
        engine = ReasoningEngine.ReasoningEngine()
        nodes = []
        rules = []
        vulens = []
        nm = nmap.PortScanner()
        logging.info('Start Scanning Network Details  ...'.format())
        # nm.scan('192.168.1.0/24', '0-65535', arguments='-sS -A -sV')
        for subnet in subnets:
            ip = subnet.ipRange
            try:
                nm.scan(ip, '0-65535', arguments='-sS -A -sV')
            except:
                e = ''
        destination = []
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        destination.append(external_ip)
        inet = Node.Node("Internet", "Internet", "Attacker's location", [], 'inet')
        nodes.append(inet)
        for host in nm.all_hosts():
            name = nm[host]['hostnames'][0]['name']
            ip = nm[host]['addresses']['ipv4']
            if name == '':
                name = ip
            destination.append(name)
        for host in nm.all_hosts():
            # print('----------------------------------------------------')
            # print('Host : %s ' % nm[host]['hostnames'][0]['name'])
            # print('IP : %s ' % nm[host]['addresses']['ipv4'])
            # print('State : %s' % nm[host]['status']['state'])
            name = nm[host]['hostnames'][0]['name']
            ip = nm[host]['addresses']['ipv4']
            if name == '':
                name = ip
            label = ''
            desc = ''
            try:
                if nm[host]['osmatch']:
                    for os in nm[host]['osmatch']:
                        #print('Name : %s' % os['name'])
                        label = os['name']
                        desc = os['osclass'][0]['type']
            except:
                # print("No osmatch")
                e = ''
            lport = []
            try:
                protocols.append(nm[host]['tcp'])
            except:
                # print('No TCP')
                e = ''
            try:
                protocols.append(nm[host]['udp'])
            except:
                # print('No UDP')
                e = ''
            vuls = []
            ports = []
            protocols = ['tcp', 'udp']
            for protocol in protocols:
                lport = list(nm[host]['tcp'].keys())
                sorted(lport)
                for port in lport:
                    if nm[host]['tcp'][port]['state'] == 'open':
                        state = nm[host]['tcp'][port]['state']
                        name = nm[host]['tcp'][port]['name']
                        version = nm[host]['tcp'][port]['version']
                        cve = dal.getVulnerabilityByName(name, version)
                        if cve is not None:
                            cve_id = cve['cve']['CVE_data_meta']['ID']
                            cve_desc = cve['cve']['description']['description_data'][0]['value']
                            impact = cve['impact']['baseMetricV2']['cvssV2']['availabilityImpact']
                            cve_av = cve['impact']['baseMetricV2']['cvssV2']['accessVector']
                            auth = cve['impact']['baseMetricV2']['cvssV2']['authentication']
                            priv = ''
                            try:
                                priv = cve['impact']['baseMetricV3']['cvssV3']['privilegesRequired']
                            except:
                                # print("No cvss3")
                                e = ''
                            if priv != '':
                                auth = ''
                            cve_requires = engine.getPrivPost(cve_desc, cve_av, auth, priv)
                            cve_provides = engine.getPrivPre(cve_desc, impact, cve_requires)
                            tempVul = Vulnerability(cve_id, '', cve_desc, cve_requires, cve_provides, cve_av)
                            vuls.append(tempVul)
                            vulens.append(tempVul)
                            ports.append(port)
                        # print('port : %s\tstate : %s\tname: %s\tversion : %s' % (port, state, name, version))
                rule = {'source': [name], 'destination': destination, 'ports': ports}
                rules.append(rule)
            node = Node.Node(name, label, desc, vuls, name)
            nodes.append(node)
        # print('----------------------------------------------------')
        # print(nm.csv())
        logging.info('Finished Scanning Network Details  ...'.format())
        reachability = Reachability.Reachability(rules)
        network = {'nodes': nodes, 'vulnerabilities': vulens, 'reachabilities': [], 'subnets': subnets}
        network['reachabilities'].append(reachability)
        return network

    def __new__(cls, *args, **kwargs):
        if Scanner._instance is None:
            with Lock():
                if Scanner._instance is None:
                    Scanner._instance = super().__new__(cls, *args, **kwargs)

        return Scanner._instance

def printNetwork(network):
    for key, li in network.items():
        print(key, "=>")
        for val in li:
            print(val)

# if __name__ == "__main__":
#     js2 = {"subnets": [
#         {
#             "id": "internet",
#             "name": "Internet",
#             "desc": "Outside network",
#             "zone": "zone0",
#             "ipRange": "200.40.47.120/29"
#         },
#         {
#             "id": "sn1",
#             "name": "DMZ",
#             "desc": "Demilitarized zone",
#             "zone": "zone1",
#             "ipRange": "192.168.1.0/24"
#         },
#         {
#             "id": "sn2",
#             "name": "lan1",
#             "desc": "Internal network",
#             "zone": "zone2",
#             "ipRange": "192.168.17.0/24"
#         }
#     ],
#         "nodes": [
#             {
#                 "id": "Host0",
#                 "name": "Host0",
#                 "label": "Adversary",
#                 "desc": "Attacker's location",
#                 "roles": ["ReachabilityControlPoint"],
#                 "attributes": {"platform": "juniper"},
#                 "group": 21,
#                 "locations": [
#                     {"ip": "200.40.47.122", "subnetId": "internet"},
#                     {"ip": "192.168.1.1", "subnetId": "sn1"},
#                     {"ip": "192.168.17.1", "subnetId": "sn2"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "6.8", "ports": ["22"]},
#                     {"id": "1", "score": "6.8", "ports": ["8080"]}
#                 ]
#             },
#             {
#                 "id": "Host1",
#                 "name": "Host1",
#                 "label": "Host1",
#                 "desc": "Host1",
#                 "roles": ["Host1"],
#                 "attributes": {"platform": "linux"},
#                 "group": 1,
#                 "locations": [
#                     {"ip": "192.168.1.50", "subnetId": "sn1"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "6.8", "ports": ["22"]},
#                     {"id": "1", "score": "6.8", "ports": ["8080"]},
#                     {"id": "3", "score": "6.8", "ports": ["*"]},
#                     {"id": "4", "score": "6.8", "ports": ["*"]}
#                 ]
#             },
#             {
#                 "id": "Host2",
#                 "name": "Host2",
#                 "label": "Host2",
#                 "desc": "Host2",
#                 "roles": ["Host2"],
#                 "attributes": {"platform": "linux"},
#                 "group": 1,
#                 "locations": [
#                     {"ip": "192.168.1.75", "subnetId": "sn1"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["*"]},
#                     {"id": "4", "score": "6.8", "ports": ["*"]}
#                 ]
#             }
#         ],
#         "vulnerabilities": [
#             {
#                 "id": "2",
#                 "score": "7.3",
#                 "externalId": "CVE-2013-07-15",
#                 "source": "CVE",
#                 "cvss2": "7.3",
#                 "shortDesc": "ftp_rhost",
#                 "description": "Using an ftp vulnerability, the intruder creates an .rhosts file in the ftp home directory, creating a remote login trust relationship between his machine and the target machine. This attack is stealthy",
#                 "type": "injection",
#                 "requires": "none",
#                 "provides": "app_user_priv",
#                 "vector": "remote"
#             },
#             {
#                 "id": "3",
#                 "score": "9.5",
#                 "externalId": "CVE-2015-01-01",
#                 "source": "CVE",
#                 "cvss2": "9.5",
#                 "shortDesc": "remote login",
#                 "description": "Using an existing remote login trust relationship between two machines, the intruder logs into from one machine to another and get a user shell without supplying a password. This attack is detectable.",
#                 "type": "remote login",
#                 "requires": "app_user_priv",
#                 "provides": "sys_root_priv",
#                 "vector": "local"
#             },
#             {
#                 "id": "1",
#                 "score": "6.8",
#                 "externalId": "CVE-2009-10-15",
#                 "source": "CVE",
#                 "cvss2": "6.8",
#                 "shortDesc": "SSH buffer overflow",
#                 "description": "This vulnerability allows a remote attacker to establish an SSH connection to the remote host via a buffer overflow insertion method.",
#                 "type": "buffer_overflow",
#                 "requires": "none",
#                 "provides": "app_user_priv",
#                 "vector": "remote"
#             },
#             {
#                 "id": "4",
#                 "score": "9.3",
#                 "externalId": "CVE-2017-6074",
#                 "source": "CVE",
#                 "cvss2": "9.3",
#                 "cvss3": "7.8",
#                 "shortDesc": "local buffer overflow",
#                 "description": "Exploiting a buffer overflow vulnerability on a setuid root file gives attacker root access on a local machine. This attack is stealthy.",
#                 "type": "local buffer overflow",
#                 "requires": "sys_user_priv",
#                 "provides": "sys_root_priv",
#                 "vector": "local"
#             }
#         ],
#         "reachability": {
#             "defaultPolicy": "DENY",
#             "rules": [
#                 {"source": ["Host0"], "destination": ["Host1", "Host2"],
#                  "ports": ["22"], "action": "ACCEPT"},
#                 {"source": ["Host0"],
#                  "destination": ["Host1"], "ports": ["8080"], "action": "ACCEPT"},
#                 {"source": ["Host1"], "destination": ["Host0"], "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["Host1"], "destination": ["Host2"], "ports": ["22"],
#                  "action": "ACCEPT"},
#                 {"source": ["Host2"], "destination": ["Host0"], "ports": ["*"],
#                  "action": "ACCEPT"},
#                 {"source": ["Host2"],
#                  "destination": ["Host1"], "ports": ["22"],
#                  "action": "ACCEPT"}
#             ]
#         }
#     }
#     js3 = {"subnets": [
#         {
#             "id": "internet",
#             "name": "Internet",
#             "desc": "Outside network",
#             "zone": "zone0",
#             "ipRange": "200.40.47.120/29"
#         },
#         {
#             "id": "sn1",
#             "name": "DMZ",
#             "desc": "Demilitarized zone",
#             "zone": "zone1",
#             "ipRange": "192.168.1.0/24"
#         },
#         {
#             "id": "sn2",
#             "name": "lan1",
#             "desc": "Internal network",
#             "zone": "zone2",
#             "ipRange": "192.168.17.0/24"
#         }
#     ],
#         "nodes": [
#             {
#                 "id": "inet",
#                 "name": "Internet",
#                 "label": "Internet",
#                 "desc": "Attacker's location",
#                 "roles": ["Internet"],
#                 "group": 0,
#                 "locations": [
#                     {"ip": "200.40.47.121", "subnetId": "internet"}
#                 ],
#                 "vulnerabilities": []
#             },
#             {
#                 "id": "AdministratorServer",
#                 "name": "Administrator Server",
#                 "label": "Administrator Server",
#                 "desc": "Administrator Server",
#                 "roles": ["Administrator Server"],
#                 "attributes": {"platform": "juniper"},
#                 "group": 21,
#                 "locations": [
#                     {"ip": "200.40.47.122", "subnetId": "internet"},
#                     {"ip": "192.168.1.1", "subnetId": "sn1"},
#                     {"ip": "192.168.17.1", "subnetId": "sn2"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
#                     {"id": "1", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["22"]},
#                     {"id": "4", "score": "6.8", "ports": ["22"]},
#                     {"id": "5", "score": "6.8", "ports": ["22"]},
#                     {"id": "6", "score": "6.8", "ports": ["22"]}
#                 ]
#             },
#             {
#                 "id": "LocalDesktop",
#                 "name": "Local Desktop",
#                 "label": "Local Desktop",
#                 "desc": "Local Desktop",
#                 "roles": ["Local Desktop"],
#                 "attributes": {"platform": "linux"},
#                 "group": 1,
#                 "locations": [
#                     {"ip": "192.168.1.50", "subnetId": "sn1"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
#                     {"id": "1", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["22"]},
#                     {"id": "4", "score": "6.8", "ports": ["22"]},
#                     {"id": "5", "score": "6.8", "ports": ["22"]},
#                     {"id": "6", "score": "6.8", "ports": ["22"]}
#                 ]
#             },
#             {
#                 "id": "GatewayServer",
#                 "name": "Gateway Server",
#                 "label": "Gateway Server",
#                 "desc": "Gateway Server",
#                 "roles": ["Gateway Server"],
#                 "attributes": {"platform": "linux"},
#                 "group": 1,
#                 "locations": [
#                     {"ip": "192.168.1.75", "subnetId": "sn1"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "3", "score": "6.8", "ports": ["22"]}
#                 ]
#             },
#             {
#                 "id": "MailServer",
#                 "name": "Mail Server",
#                 "label": "Mail Server",
#                 "desc": "Mail Server",
#                 "roles": ["Mail Server"],
#                 "attributes": {"platform": "linux"},
#                 "group": 1,
#                 "locations": [
#                     {"ip": "192.168.1.90", "subnetId": "sn1"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
#                     {"id": "1", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["22"]},
#                     {"id": "4", "score": "6.8", "ports": ["22"]},
#                     {"id": "5", "score": "6.8", "ports": ["22"]},
#                     {"id": "6", "score": "6.8", "ports": ["22"]}
#                 ]
#             },
#             {
#                 "id": "SQLServer",
#                 "name": "SQL Server",
#                 "label": "SQL Server",
#                 "desc": "SQL Server",
#                 "roles": ["SQL Server"],
#                 "attributes": {"platform": "macos"},
#                 "group": 2,
#                 "locations": [
#                     {"ip": "192.168.17.5", "subnetId": "sn2"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
#                     {"id": "1", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["22"]},
#                     {"id": "4", "score": "6.8", "ports": ["22"]},
#                     {"id": "5", "score": "6.8", "ports": ["22"]},
#                     {"id": "6", "score": "6.8", "ports": ["22"]}
#                 ]
#             },
#             {
#                 "id": "WebServer",
#                 "name": "Web Server",
#                 "label": "Web Server",
#                 "desc": "Web Server",
#                 "roles": ["Web Server"],
#                 "attributes": {"platform": "linux"},
#                 "group": 2,
#                 "locations": [
#                     {"ip": "192.168.17.20", "subnetId": "sn2"}
#                 ],
#                 "vulnerabilities": [
#                     {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
#                     {"id": "1", "score": "6.8", "ports": ["22"]},
#                     {"id": "3", "score": "6.8", "ports": ["22"]},
#                     {"id": "4", "score": "6.8", "ports": ["22"]},
#                     {"id": "5", "score": "6.8", "ports": ["22"]},
#                     {"id": "6", "score": "6.8", "ports": ["22"]}
#                 ]
#             }
#         ],
#         "vulnerabilities": [
#             {
#                 "id": "1",
#                 "score": "7.3",
#                 "externalId": "CVE-2009-0568",
#                 "source": "CVE",
#                 "cvss2": "7.3",
#                 "shortDesc": "RPC Marshalling Engine Vulnerability",
#                 "description": "This vulnerability allows a remote attacker to bypass the PHP authentication process via an SQL injection attack and obtain access as a registered user.",
#                 "type": "injection",
#                 "requires": "app_user_priv",
#                 "provides": "sys_user_priv",
#                 "vector": "remote"
#             },
#             {
#                 "id": "2",
#                 "score": "9.5",
#                 "externalId": "CVE-2008-0015",
#                 "source": "CVE",
#                 "cvss2": "9.5",
#                 "shortDesc": "Microsoft Video ActiveX Control Vulnerability",
#                 "description": "This vulnerability allows an authenticated user to inject system commands via malformed requests sent to the PHP server.",
#                 "type": "injection",
#                 "requires": "none",
#                 "provides": "sys_root_priv",
#                 "vector": "local"
#             },
#             {
#                 "id": "3",
#                 "score": "6.8",
#                 "externalId": "CVE-2012-6066",
#                 "source": "CVE",
#                 "cvss2": "6.8",
#                 "shortDesc": "FreeSSHd Authentication Bypass",
#                 "description": "This vulnerability allows a remote attacker to establish an SSH connection to the remote host via a buffer overflow insertion method.",
#                 "type": "buffer_overflow",
#                 "requires": "none",
#                 "provides": "sys_user_priv",
#                 "vector": "remote"
#             },
#             {
#                 "id": "4",
#                 "score": "9.3",
#                 "externalId": "CVE-2011-4040",
#                 "source": "CVE",
#                 "cvss2": "9.3",
#                 "cvss3": "7.8",
#                 "shortDesc": "MiniSMTP Server Remote Stack BOF",
#                 "description": "The dccp_rcv_state_process function in net/dccp/input.c in the Linux kernel through 4.9.11 mishandles DCCP_PKT_REQUEST packet data structures in the LISTEN state, which allows local users to obtain root privileges or cause a denial of service (double free) via an application that makes an IPV6_RECVPKTINFO setsockopt system call.",
#                 "type": "escalation",
#                 "requires": "none",
#                 "provides": "sys_root_priv",
#                 "vector": "local"
#             },
#             {
#                 "id": "5",
#                 "score": "8.3",
#                 "externalId": "CVE-2015-1762",
#                 "source": "NVD",
#                 "shortDesc": "Remote Code Execution Vulnerability",
#                 "description": "SMB unauthorized resource mapping R/W.",
#                 "type": "buffer_overflow",
#                 "requires": "sys_user_priv",
#                 "provides": "sys_root_priv",
#                 "vector": "network"
#             },
#             {
#                 "id": "6",
#                 "score": "8.3",
#                 "externalId": "CVE-2010-3972",
#                 "source": "NVD",
#                 "shortDesc": "IIS FTP Service Heap BOF",
#                 "description": "SMB unauthorized resource mapping R/W.",
#                 "type": "buffer_overflow",
#                 "requires": "none",
#                 "provides": "sys_root_priv",
#                 "vector": "network"
#             }
#         ],
#         "reachability": {
#             "defaultPolicy": "DENY",
#             "rules": [
#                 {"source": ["inet"], "destination": ["MailServer", "WebServer", "LocalDesktop"],
#                  "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["LocalDesktop"],
#                  "destination": ["MailServer", "WebServer", "GatewayServer"],
#                  "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["AdministratorServer"],
#                  "destination": ["MailServer", "WebServer", "GatewayServer", "SQLServer", "LocalDesktop"],
#                  "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["GatewayServer"],
#                  "destination": ["inet"],
#                  "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["SQLServer"],
#                  "destination": ["WebServer", "AdministratorServer",
#                                  "LocalDesktop"],
#                  "ports": ["*"], "action": "ACCEPT"},
#                 {"source": ["WebServer"],
#                  "destination": ["MailServer", "inet", "GatewayServer", "SQLServer", "AdministratorServer",
#                                  "LocalDesktop"],
#                  "ports": ["*"], "action": "ACCEPT"}
#             ]
#         }
#     }

