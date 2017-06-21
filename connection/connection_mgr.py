# -*- coding: utf-8 -*-

from abc import abstractmethod
from abc import ABCMeta

from ssh_common import SshCommom
from telnet_common import TelnetCommon


__all__ = ['ConnectionMgr','global_connections']

global_connections = []

class AbstractConnetionMgr(object):

    __metaclass__ = ABCMeta

    def set_shell_prompt(self,prompt):
        old_prompt = self._current._prompt
        self._current.set_prompt(prompt)
        return old_prompt

    def set_shell_timeout(self,timeout='5'):
        return self._current.set_timeout(timeout)

    def set_shell_pausetime(self,pause='3'):
        return self._current.set_pausetime(pause)

    def get_current_connection(self):
        return self._current

    @abstractmethod
    def connect_to_host(self):
        raise NotImplementedError('should be implement first')

    @property
    def base_connection(self):
        raise NotImplementedError('should be implement first')

    def disconnect_from_host(self,conn=None):
        if conn is not None:
            if conn not in self._connections:
                raise RuntimeError('unknow connection')
            self._current = conn
        if not self._current:
            return
        if self._current in global_connections:
            global_connections.remove(conn)
        self._current.close_connection()
        if len(global_connections) == 0:
            self._current = None
        else:
            self._current = global_connections[-1]



    def disconnect_all_hosts(self):
        global global_connections
        for conn in self._connections:
            if conn in global_connections:
                global_connections.remove(conn)
            conn.close_connection
        self._connections = []
        self._current = None


    def switch_host_connection(self,conn):
        if not conn:
            raise RuntimeError('the connection you want to switch is not valid')
        if conn in self._connections:
            if conn in global_connections:
                global_connections.remove(conn)
            global_connections.append(conn)  #保持这个最新的conn是在列表的最后面
            self._current = conn
            print 'switch to connection %s' %conn
        else:
            raise RuntimeError('no such connection')

    def Execute_shell_command(self,cmd):
        self._current.write(cmd)
        return self._current.read()



class SshCommonMgr(AbstractConnetionMgr):

    def __init__(self):
        self._current = None
        self._connections = []

    @property
    def base_connection(self):
        return SshCommom

    def connect_to_host(self,host,port=22,user='Nemuadmin',password='nemuuser',prompt='$',timeout='10sec'):
        my_prompt = prompt
        conn = self.base_connection(host,port,my_prompt,timeout,'LF')
        ret = conn.login(user,password)
        #conn.set_prompt(my_prompt)

        self._current = conn
        self._connections.append(conn)
        global global_connections
        if conn not in global_connections:
            global_connections.append(conn)

        return conn

class TelnetCommonMgr(AbstractConnetionMgr):

        def __init__(self):
            self._current = None
            self._connections = []

        @property
        def base_connection(self):
            return TelnetCommon

        def connect_to_host(self,host,port=23,username='public',password='public',prompt='',timeout='20sec'):
            my_prompt = prompt
            conn = self.base_connection(host,port,my_prompt,timeout,'CRLF')
            ret = conn.login(username,password)

            self._current = conn
            self._connections.append(conn)
            global global_connections
            if conn not in global_connections:
                global_connections.append(conn)

            return conn

class connection_mgr(object):
    """
    Used to connect to host, either TELNET or SSH
    | Input Parameters  | Man. | Description |
    | host              | Yes  | the address of the host you want connect |
    | port              | No   | the port you want connect |
    | username          | No   | the username    |
    | password          | No   | the password    |
    | username_prompt    | No   | the username prompt |
    | password_prompt    | No   | the password prompt |
    | conn_type         | No   | the connection type, TELNET or SSH |
    | prompt            | No   | the command prompt of target host |
    | newline           | No   | the newline of target host , can be CRLF or LF for windows or linux |
    | timeout           | No   | the timeout of target host |
    | pausetime         | No   | the pause time before read something from connection |
    | device_type       | No   | the device_type of your target host |
    """

    def __init__(self):
        global _global_ssh_connection
        global _global_telnet_connection
        self._current_mgr = None
        self._default_mgr = _global_telnet_connection
        self._connectiondict = {'SSH':_global_ssh_connection,'TELNET':_global_telnet_connection}

    def connect_to_host(self,host,port=23,username='',password='',conn_type='TELNET',**kwargs):  #默认是telnet，所以这里初始化是用的telnet的参数
        if conn_type.upper() == 'SSH':
            username_prompt = kwargs.get('username_prompt','login: ')
            password_prompt = kwargs.get('password','password: ')
            newline = kwargs.get('newline','LF')
            prompt = '$'
        elif conn_type.upper() == 'TELNET':
            username_prompt = kwargs.get('username_prompt', 'login: ')    #这里登录telnet的也是这个prompt，如果改了需要在这里变，有点不方便，后期优化，prompt可以是一个list，里面检查就可以
            password_prompt = kwargs.get('password', 'password: ')
            newline = kwargs.get('newline', 'CRLF')
            prompt = '>'
        timeout = kwargs.get('timeout','10sec')
        pausetime = kwargs.get('pausetime','0.05sec')
        connmgr = self._connectiondict[conn_type.upper()]
        current = connmgr.base_connection(host,port,prompt,timeout,newline)
        connmgr._current = current
        login_ret = ''
        login_ret = login_ret + current.login(username,password,username_prompt,password_prompt)
        current.set_prompt(prompt)
        current.set_pausetime(pausetime)
        current.set_timeout(timeout)

        connmgr._connections.append(current)

        global global_connections
        if current not in global_connections:
            global_connections.append(current)
        print 'connect to %s success, login info is %s' %(host,login_ret)
        return current

    def get_current_mgr(self):
        global global_connections
        if len(global_connections) != 0:
            self._current_mgr = self._connectiondict[global_connections[-1].conn_type.upper()]
        else:
            self._current_mgr = self._default_mgr
        return self._current_mgr

    current_mgr = property(fget=get_current_mgr)

    def switch_to_connection(self,conn):
        if conn:
            self._current_mgr = self._connectiondict[conn.conn_type.upper()]
            return self._current_mgr.switch_host_connection(conn)
        raise RuntimeError('the connection you input is invalid')

    def disconnect_from_host(self,conn):
        global global_connections
        if conn:
            if conn in global_connections:
                global_connections.remove(conn)
            return self._connectiondict[conn.conn_type.upper()].disconnect_from_host(conn)

    def disconnect_all_hosts(self,conn_type='ALL'):
        global global_connections
        if conn_type == 'ALL':
            for mgr in self._connectiondict.values():
                mgr.disconnect_all_hosts()
            global_connections = []
        if conn_type.upper() in self._connectiondict.keys():
            connmgr = self._connectiondict[conn_type.upper()]
            for conn in connmgr._connections:
                if conn in global_connections:
                    global_connections.remove(conn)
            return connmgr.disconnect_all_hosts()

    def Execute_shell_command(self,cmd):
        return self.current_mgr.Execute_shell_command(cmd)

_global_ssh_connection = SshCommonMgr()
_global_telnet_connection = TelnetCommonMgr()


if __name__ == '__main__':
    c = connection_mgr()
    host1 = '10.68.160.240'
    username1 = 'Nemuadmin'
    password1 = 'nemuuser'
    host2 = '10.56.127.6'
    username2 = 'tdlte-tester'
    password2 = 'btstest'
    a = c.connect_to_host(host2,23,username2,password2)
    print c.current_mgr.Execute_shell_command('ls')
    b = c.connect_to_host(host1,port=22,username=username1,password=password1,conn_type='SSH')
    print c.current_mgr.Execute_shell_command('ls')
    c.disconnect_all_hosts()



