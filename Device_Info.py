import psutil, platform, json

### Define the empty JSON object ###
sys_info = {}

### CPU Info Block ###
cpufreq = psutil.cpu_freq()
sys_info["CPUs"] = {
    "Description": f"{platform.processor()} @ {cpufreq.max/1000:.2f}Ghz",
    "Cores": psutil.cpu_count(logical=False)
}

### Memory Info Block ###
svmem = psutil.virtual_memory()
sys_info["Memory"] = {
    "InstalledGB": int(round(svmem.total/1000000000,0)),
    "AvailableGB": int(round(svmem.available/1000000000,0))
}

### Storage Info Block ###
sys_info["Storage"] = []
storage = sys_info["Storage"]
partitions = psutil.disk_partitions()
disk_available = 0
for partition in partitions:
    partition_usage = psutil.disk_usage(partition.mountpoint)
    storage.append({"Description":partition.device,
                    "CapacityGB": partition_usage.total/1000000000,
                    "AvailableGB":partition_usage.free/1000000000,
                    "Type":"SSD"})

# print(storage)

### Network Info ###
sys_info['Network'] = []
network = sys_info['Network']
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        if str(address.family) == 'AddressFamily.AF_INET':
            network.append({"Description":interface_name,
                            "IP Address":address.address,
                            "Netmask" : address.netmask
                            })
        elif  str(address.family) == 'AddressFamily.AF_PACKET':
            network.append({"Description":interface_name,
                            "IP Address":address.address,
                            "Netmask" : address.netmask
                            })
# print(network)

# print(sys_info)

### Export dictionary to JSON File ###
with open("output.json","w") as newfile:
    json.dump(sys_info,newfile)