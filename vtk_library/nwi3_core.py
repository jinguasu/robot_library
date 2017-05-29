import commands, re,os,time
from subprocess import *
from subprocess import Popen
from threading  import Thread
from is_nwi3core_started import _is_nwi3core_started
#from nwi3_print_helper import Nwi3_print_output


class nwi3_core(object):
	def __init__(self):
		pass
		
	def start_nwi3_core(self,waiting_time=5):
		process_name = 'vtk-implementation-common-nwi3core.jar'
		process_name_path = '/var/nwi3_vtk/lib/'
		if _is_nwi3core_started(process_name):
			print "****nwi3core service has been started! No need to start nwi3core again!****"
		else:
			self.p = Popen(["java", "-jar", process_name_path + process_name],stdin=PIPE,stdout=PIPE,stderr=PIPE)
			print "*****nwi3core service started with process id is %s" %self.p
			pid = self.p.pid


	def stop_nwi3_core(self):
		process_name = 'vtk-implementation-common-nwi3core.jar'
		cmd = 'ps aux | grep %s | grep -v grep' %process_name
		output = commands.getoutput(cmd)
		a =output.split(' ')
		cmd = 'kill -9 %s' %a[5]
		os.system(cmd)
		print 'nwi3core service is killed'
	
	def list_rigistered_element(self):
		self.start_nwi3_core()
		NE_list = []
		self.p.stdin.write("1"+"\n");
		self.p.stdin.write("0"+"\n");
		time.sleep(2)
		output_line = self.p.stdout.readlines()
		for line in output_line:
			line = line.strip()
			NE_ID = re.match(r'NE-OMS-(\d+)*',line)
			if NE_ID != None:
				NE_list.append('NE-OMS-'+NE_ID.group(1))
		return NE_list
		
		
if __name__ == '__main__':
	core = nwi3_core()
	process_name = 'vtk-implementation-common-nwi3core.jar'
	print _is_nwi3core_started(process_name)
	if _is_nwi3core_started(process_name):
		core.stop_nwi3_core()
		core.start_nwi3_core()
		print _is_nwi3core_started(process_name)
		core.list_rigistered_element()
	else:
		core.start_nwi3_core()
		print _is_nwi3core_started(process_name)
		core.list_rigistered_element()
	print _is_nwi3core_started(process_name)
		
		
		
		
		
		
		