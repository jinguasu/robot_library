# -*- coding: utf-8 -*-

import re

#from robot.utils import timestr_to_secs
#from robot.utils import secs_to_timestr

def timestr_to_secs(str):
    a = re.match(r'(\d+).*',str)
    return float(a.group(1))

def secs_to_timestr(num):
    return str(num)+'sec'

import time
import socket

class SshCommom(object):

    def __init__(self,host,port,prompt,timeout='10sec',newline='CRLF'):
        try:
            import paramiko
        except:
            raise Exception ("can't import paramiko, SSH can't use")
        self.host = host
        self.port = port
        self._timeout = timestr_to_secs(timeout)
        self._newline = None
        self.set_newline(newline.upper().replace('LF','\n').replace('CR','\r'))
        self._prompt = None
        self.set_prompt(prompt)

        self.username = None
        self.password = None

        self._pausetime = 0.05
        self.conn_type = 'SSH'
        self.device_type = None

        self._channel = None
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    @property   #装饰器，将这个方法变为这个类的一个属性，可以直接.channel调用，不需要像普通的方法一样后面要加括号channel()
    def channel(self):
        if not self._channel:   #如果这个时候没有打开的通道，就打开一个
            self._channel = self.client.invoke_shell()   #启动SSH  shell 交互通道，并且返回这个通道可以写入数据并且读取数据
            self._channel.set_combine_stderr(True)   #这里写成true 就可以在后面的channel.recv里也收到标准错误的数据了
        return self._channel      #返回这时候已经是代表通道的self._channel了

    def login(self,username,password,login_prompt='login: ',password_prompt='Password: ',key_filename=None):
        self.username = username
        self.password = password
        self.key_filename = key_filename         #  这里需要解释 ，现在还不清楚,这里是认证信息，但是这里没有，所以我们就随便写了个key_filename，于是这里用不到会校验失败，然后就会用到之前的set_missing_key来登录

        if key_filename != None:
            self.client.connect(self.host,self.port,username,key_filename=self.key_filename,timeout=self._timeout)  #这里用刀了认证的key_filename，所以这里没有用到密码
        else:
            self.client.connect(self.host,self.port,username,password,timeout=self._timeout)
        time.sleep(self._pausetime)
        start_time = time.time()
        login_ret = ''
        while time.time() - start_time < int(self._timeout):
            if self.channel.recv_ready():
                c = self.channel.recv(128)
                if c == '':
                    raise Exception("no any returns after connect")
                else:
                    login_ret = login_ret + c
                    continue
            else:
                time.sleep(0.00005)   # 可能机器卡还没开始读取，等一下再继续循环

        time.sleep(self._pausetime)
        if self.channel.recv_ready():
            login_ret = login_ret + self.channel.recv(1024)
        if login_ret[-10:].find(self._prompt) == -1:    #这里从最后10位开始查找是否包含我们设置的prompt，查找不到返回-1，查找到了返回所在的ID位置
            raise AssertionError('No match found for prompt %s' %self._prompt)
        else:
            print ("Select pattern '%s' as default pattern" % self._prompt)
        #self.set_prompt(pattern)
        return login_ret

    def write_bare(self,text):   #这里是向打开的SSH通道输入命令，但是不包含回车换行，需要我们自己添加
        try:
            text = str(text)  # 将输入的命令转换为字符串
        except UnicodeDecodeError:
            msg = 'only ascii characters are allowed in SSH, got: %s' %text
            raise ValueError(msg)

        self.channel.sendall(text)

    def write(self,text):
        self.write_bare(text)
        if self._newline is None:
           self.write_bare('')
        else:
            self.write_bare(self._newline)


    def read(self):  #当输入命令后立刻读取输出的数据，而不是等到prompt出现的时候
        time.sleep(self._pausetime)
        if self.channel is None:
            return ''
        data = ''
        #print self.channel.recv_ready()
        while self.channel.recv_ready():
            data = data + self.channel.recv(10000)

        #print data[-10:]
        #if data[-80:].find(self._prompt) == -1:    #这里从最后10位开始查找是否包含我们设置的prompt，查找不到返回-1，查找到了返回所在的ID位置
         #   raise AssertionError('No match found for prompt %s' %self._prompt)
        #else:
         #   return data
        return data
    def close_connection(self):
        self.client.close()
        self.client = None
        self._channel = None
        print "Disconnect from this sever"
        return

    @property
    def connected(self):
        try:
            # print dir(self.channel)
            if not self.channel.active or self.channel.closed:
                return False
            else:
                return True
            # return False if self.channel.closed else True
        except socket.error:
            return False
        except Exception as _:
            return False
        else:
            return True


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




if __name__ == '__main__':
    host = '10.68.160.240'
    username = 'Nemuadmin'
    password = 'nemuuser'
    ssh = SshCommom(host,22,'$',newline='LF')
    print ssh.login(username,password)
    ssh.set_prompt(':')
    ssh.write('su -')
    print ssh.read()
    ssh.write('nsn')
    ssh.set_prompt('#')
    print ssh.read()
    ssh.close_connection()
    print ssh.connected
