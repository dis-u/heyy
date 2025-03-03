# network_monitor.py
import psutil

def get_active_networks():
    networks = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.raddr:
            networks.append({"ip": conn.raddr.ip, "port": conn.raddr.port})
    return networks
