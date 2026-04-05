# network_tools.py
import ipaddress

def get_hosts(network_cidr="192.168.10.0/26"):
    """
    Retourne une liste des hôtes disponibles dans le réseau donné.
    """
    network = ipaddress.ip_network(network_cidr)
    hosts = [str(host) for host in network.hosts()]
    return hosts

def save_hosts_to_file(hosts, filename="hosts.txt"):
    """
    Sauvegarde la liste des hôtes dans un fichier texte.
    """
    with open(filename, "w") as f:
        for host in hosts:
            f.write(host + "\n")

if __name__ == "__main__":
    hosts = get_hosts()
    print("Hôtes disponibles :", hosts)
    save_hosts_to_file(hosts)
    print(f"Liste des hôtes sauvegardée dans hosts.txt")