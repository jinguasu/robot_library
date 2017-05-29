# -*- coding: utf-8 -*-

import telnetlib, time


from robot.utils import timestr_to_secs
from robot.utils import secs_to_timestr


class TelnetCommon(telnetlib.Telnet):

    def __init__(self,host,port,prompt,timeout='10sec',newline='CRLF'):

        self.host = host
        self.port = port == '' and 23 or int(port)
        self._timeout = timestr_to_secs(timeout)
        self._telnet = telnetlib.Telnet(self.host,self.port)
        self._newline = None
        self.set_newline(newline.upper().replace('LF','\n').replace('CR','\r'))
        self._prompt = None
        self.set_prompt(prompt)

        self.username = None
        self.password = None

        self._pausetime = 0.05
        self.conn_type = 'TELNET'


    def set_pausetime(self,pause):
        old = secs_to_timestr(self._pausetime)
        self._pausetime = timestr_to_secs(pause)
        return old       # 这里都要返回old的原因是之后要返回去这个类原来的这些变量的值，类中的变量是可以被改变的，所以我们要恢复，这里保存好，为以后做准备。

    def set_newline(self,newline):
        old = self._newline
        self._newline = newline
        return old

    def set_timeout(self,timeout):
        old = secs_to_timestr(self._timeout)
        self._timeout = timestr_to_secs(timeout)
        return old

    def set_prompt(self,prompt):
        """Sets the prompt used in this connection to 'prompt'.
        'prompt' can also be a list of regular expressions
        """
        old_prompt = self._prompt
        self._prompt = prompt
        return old_prompt

    def write(self,text):
        try:
            text = str(text)
        except:
            msg = 'only ascii characters are allowed in telnet. got %s' % text
            raise ValueError(msg)
        self._telnet.write(text + self._newline)
        #return self._telnet.read_until(self._prompt)

    def read(self):
        return self._telnet.read_until(self._prompt)

    def login(self,username='',password='',login_prompt='ogin: ',password_prompt='assword: '):

         self.username = username
         self.password = password

         ret = ''
         if username != '':
             ori_prompt = self.set_prompt(login_prompt)
             self._telnet.read_until(self._prompt)
             self._telnet.write(username + self._newline)
             self.set_prompt(ori_prompt)
         if password != '':
             ori_prompt = self.set_prompt(password_prompt)
             self._telnet.read_until(self._prompt)
             self._telnet.write(password + self._newline)
             self.set_prompt(ori_prompt)
         return self._telnet.read_until(self._prompt)

    def close_connection(self):
        self._telnet.close()
        #ret = self.read()
        #print ret
        print 'disconnect from this sever '
        return

    def __del__(self):
        pass

if __name__ == '__main__':
    host = '10.56.127.6'
    username = 'tdlte-tester'
    password = 'btstest'
    tn = TelnetCommon(host,23,'>','2')
    tn.login(username,password)
    print tn.write('ls')
    tn.close_connection()














