# -*- coding: utf-8 -*-
import platform
from connection.connection_mgr import connection_mgr
#conn = connection_mgr()
#host2 = '10.56.127.6'
#username2 = 'tdlte-tester'
#password2 = 'btstest'
#conn.connect_to_host(host2,23,username2,password2)

def get_os_platform_version(with_connection=True):
    if with_connection is True:
        cmd = 'python -c "import platform;print platform.platform()"'
        ret = connection_mgr().Execute_shell_command(cmd)
        print ret
    else:
        return platform.platform()

print get_os_platform_version()

