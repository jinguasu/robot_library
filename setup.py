# -*- coding: utf-8 -*-
import time,os,subprocess,re


class setup(object):

	def __init__(self):
		pass
		
	def get_timestamp(self,timeformat="%Y%m%d%H%M%S"):
		return time.strftime(timeformat)
	
	def replace_string(self,string,a,b):
		if a in string:
			f = string.replace(a,b)
			return f
		else:
			return string
	
	def create_dir(self,string):
		os.makedirs(string)
		
	def ping_eNB_should_success(self,ip):
		a = 0
		p = subprocess.Popen(['ping',ip,'-n','1'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		p_output = p.stdout.readlines()
		for i in p_output:
			i = i.strip()
			if i.find('unreachable') != -1 or i.find('timed out') != -1:
				a = 1
		if a == 0:
			return True
		else:
			return False

	def get_activate_sw_version(self,host='10.68.179.230',port=22,username='toor4nsn',password='oZPS0POrRieRtu'):
		try:
			import paramiko
		except:
			raise Exception("can't import paramiko")
		self.host = host
		self.username = username
		self.password = password
		self.port = port
		s = paramiko.SSHClient()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(self.host, self.port, self.username, self.password)
		stdin, stdout, stderr = s.exec_command('ls /ffs/run')
		for i in stdout.readlines():
			sw = i.strip()
			sw_version = re.match(r'TargetBD_(.*).xml',sw)
			if sw_version != None:
				print 'the current sw package is %s' % sw_version.group(1)
				break
		s.close()
