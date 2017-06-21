# -*- coding: utf-8 -*-

from connection_mgr import connection_mgr
global_connection_mgr = connection_mgr()

def switch_host_connection(conn):
    return global_connection_mgr.switch_to_connection(conn)

def execute_shell_command(command):
    return global_connection_mgr.Execute_shell_command(command)

def disconnect_all_hosts():
    return global_connection_mgr.disconnect_all_hosts()

def disconnect_from_host(conn):
    return global_connection_mgr.disconnect_from_host(conn)

def get_current_connection():
    return global_connection_mgr.get_current_mgr()

def connect_to_host(host,port,username,password):
    return global_connection_mgr.connect_to_host(host,port,username,password)


