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


# Returns a dictionary of dictionaries.
# Each interface has an entry with keys 'all' and 'ipv4'
def ip_a():
    output = get_output('ip a')
    # Split each interface and remove empty entries
    split_output = re.split('^\d: |\\n\d: ', output)
    split_output.remove('')
    # Hash to store all interfaces with info about them
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

    
