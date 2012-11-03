#!/usr/bin/python
from locale import getdefaultlocale as dlocale
import subprocess
import re

# Get the standard output of a command as a string
def get_output(command):
    # Get default locale encoding
    encoding = dlocale()[1]
    # Get output of command as byte code
    stdout = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read()
    # Convert byte to string
    return str(stdout.decode(encoding))


# Get interfaces with assigned ipv4 addresses
# Returns a dictionary of dictionaries.
# Each interface has an entry with keys 'all' (a string) 
# and 'ipv4' (A list of IPs)
def ip_a():
    output = get_output('ip a')
    # Split each interface and remove empty entries
    split_output = re.split('^\d: |\\n\d: ', output)
    split_output.remove('')
    # Dictionary to store all interfaces with info about them
    interfaces = {}
    # Compile info from output into dictionary only if it has an ipv4
    for entry in split_output:
        # Find info we want
        name = re.search('^\w+', entry).group()
        ipv4 = re.findall('inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', entry)
        if not ipv4: continue
        # Map them
        interfaces[name] = {'all': entry, 'ipv4': ipv4}
    return interfaces


# Argument is a list of interfaces
def ip_s_link(int_list):
    output = get_output('ip -s link')
    # Split each interface and remove empty entries
    split_output = re.split('^\d: |\\n\d: ', output)
    split_output.remove('')
    # Dictionary to store data
    data = {}
    # Compile info from output if it's in int_list
    for entry in split_output:
        # Find info we want
        name = re.search('^\w+', entry).group()
        if not any(name in s for s in int_list): continue
        rx_regex = 'RX:.*\\n\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)'
        tx_regex = 'TX:.*\\n\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)'
        keys = ['rx_bytes', 'rx_packets', 'rx_errors', 'rx_dropped',\
        'rx_overrun', 'rx_mcast',\
        'tx_bytes', 'tx_packets', 'tx_errors', 'tx_dropped',\
        'tx_carrier', 'tx_collsns']
        values = list(re.search(rx_regex, entry).groups())
        values.extend(list(re.search(tx_regex, entry).groups()))
        # Map the stuff
        data[name] = dict(zip(keys, values))
    return data


def netstat_s(sect_list):
    output = get_output('netstat -s')
    # Split each section up and remove empty entries
    data = {}
    section = ''
    for line in output.split('\n'):
        if re.match('^\w+:', line)
            section = line.strip(':')
            # If the section matches any of the sections in sect_list
            if any(section.lower() in s.lower() for s in sect_list):
                data[section] = {}
            else:
                section = ''
        elif section != '':
            
    return output
