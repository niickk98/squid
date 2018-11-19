'''
Squid Installer
Author: admin@hostonnet.com
Blog: https://blog.hostonnet.com
'''

from fabric.api import *

def print("Installing Squid")
    os_name = run("cat /etc/*issue")
    if not os_name.startswith("Ubuntu 16"):
        print("Script only run on Ubuntu 16.04 and 16.10")
        quit()
    run("/usr/bin/wget https://raw.githubusercontent.com/niickk98/squid/master/squid3-install.sh -O squid3-install.sh")
    run("chmod 755 squid3-install.sh")
    sudo("/bin/sh squid3-install.sh")
    print("squid installed")
