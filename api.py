from fastapi import FastAPI, Query
from pydantic import BaseModel
import ipaddress
from network_tools import get_hosts

app = FastAPI(title="Network Tools API")


@app.get("/hosts")
def hosts_default():
    hosts = get_hosts()
    return {"network": "192.168.10.0/26", "hosts": hosts}


@app.get("/count_hosts")
def count_hosts(network: str = Query(..., description="Adresse réseau"),
                cidr: int = Query(..., ge=0, le=32, description="Masque CIDR")):
    try:
        net = ipaddress.ip_network(f"{network}/{cidr}")
        num_hosts = net.num_addresses - 2  
        if num_hosts < 0:
            num_hosts = 0
        return {
            "network": str(net.network_address),
            "cidr": cidr,
            "usable_hosts": num_hosts
        }
    except ValueError as e:
        return {"error": str(e)}