""" This module is the master daemon runner.
"""

from service.runners import probe_runner

def run_daemons():
    probe_runner.run()

def check_daemon_health():
    pass

