import os
import platform
import sys
import subprocess

def ping(hostname, timeout, attempts):
    if platform.system() == "Windows":
        command = "ping {0} -n {1} -w {2}".format(
            hostname,
            attempts,
            str(timeout*1000)
        )
    else:
        command = "ping -i {0} -c {1} {2}".format(
            str(timeout),
            attempts,
            hostname
        )

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = str(process.stdout.read())

    return output

def is_online(
    ip_address,
    timeout=4,
    attempts=4,
    check_type='ping',
):
    conclusion = None
    output = None

    if check_type == 'ping':
        output = ping(ip_address, timeout, attempts)

        if 'Reply from {ip_address}:'.format(
            ip_address=ip_address,
        ) in output:
            conclusion = True
        else:
            conclusion = False

    elif check_type == 'telnet':
        pass

    return conclusion, output
