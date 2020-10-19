# This is the perimeter app's default probe runner.
# This program is built on the assumption that the perimeter django application is running with all of the following applications:
#   perimeter_core
#   perimeter_daemon
# 
# It makes calls on the perimeter daemon to probe the status of nodes, and then it logs the results to the daemon_cache_db.
# 
# By default, it is the de-facto way of actually interacting with the perimeter daemon. You can, however, make direct requests
# if you really want to and you understand what you're doing and why. 
# 
#  

import urllib

# TODO: Implement a method called node_prober which does the following 
#   1. Gets a list of all nodes from the perimeter_core web application.
#   2. Calls the relevant prober/logger for each node in the perimeter_daemon application.
# 
# Note that this service will NOT provide any form of output or user response per say.
# If it runs fine, then you can assume everything is okay.
# 
# If an exceptional condition occurs, this service is meant to log it for the developers to see. 

def run():
    while True:
        try:
            request = urllib.request.urlopen('http://127.0.0.1:8000/perimeter/daemon/infrastructure_monitoring/')
            print(request)
            sleep(2)
        except:
            pass