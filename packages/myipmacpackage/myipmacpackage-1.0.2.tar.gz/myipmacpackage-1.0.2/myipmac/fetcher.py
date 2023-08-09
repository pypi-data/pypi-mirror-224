import platform
import socket
import re
import subprocess
import mysql.connector

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def store_in_database(ip_address, mac_address):
    connection = mysql.connector.connect(
        host="13.232.178.218",
        user="testmanager",
        port="3366",
        password="tmuser20@#",
        database="ip_test"
    )
    
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS table1 (ip_address VARCHAR(15), mac_address VARCHAR(17))")
    cursor.execute("INSERT INTO table1 (ip_address, mac_address) VALUES (%s, %s)", (ip_address, mac_address))
    connection.commit()
    connection.close()

def get_mac_address():
    system = platform.system()

    if system == "Windows":
        return get_windows_mac_address()
    elif system == "Darwin":
        return get_macos_mac_address()
    elif system == "Linux":
        return get_linux_mac_address()
    else:
        return "Unknown OS"

def get_windows_mac_address():
    cmd_output = subprocess.check_output(["ipconfig", "/all"]).decode("utf-8")
    mac_search = re.search(r"Physical Address[ .]*: ([\w-]+)", cmd_output)
    if mac_search:
        return mac_search.group(1).replace("-", ":")
    else:
        return "MAC address not found"

def get_macos_mac_address():
    cmd_output = subprocess.check_output(["ifconfig"]).decode("utf-8")
    mac_search = re.search(r"ether ([\w:]+)", cmd_output)
    if mac_search:
        return mac_search.group(1)
    else:
        return "MAC address not found"

def get_linux_mac_address():
    cmd_output = subprocess.check_output(["ifconfig"]).decode("utf-8")
    mac_search = re.search(r"ether ([\w:]+)", cmd_output)
    if mac_search:
        return mac_search.group(1)
    else:
        return "MAC address not found"

def fetch_and_store():
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    
    store_in_database(ip_address, mac_address)
    print("IP and MAC addresses stored in the MariaDB database.")

if __name__ == "__main__":
    fetch_and_store()

