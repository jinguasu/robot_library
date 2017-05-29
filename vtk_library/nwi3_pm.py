from check_port import *
from subprocess import *
from nwi3_core import *
import re, os, sys


class nwi3_pm(object):
	
	def __init__(self):
		pass
	
	def vtk_verification_for_many_NEs(self,systemID_list=[]):
		if not len(systemID_list):
			print "no test NE found...."
			raise Exception("no NE found")
		default_port_for_pmvtk = 49154
		for systemID in systemID_list:
			warning_num = 0
			file_num = 0
			error_num = 0
			result_file_name = ''
			print "*****start verification for %s *****" %systemID
			if is_port_free(default_port_for_pmvtk):
				port = default_port_for_pmvtk
			else:
				port = find_port()
			if port == None:
				print "*****No free port found for PMVTK!"
				raise Exception("No free port can be used!")
			file_num,warning_num,error_num,result_file_name = self.start_pm_upload_process(systemID,port)
			print "this %s upload %s counter to VTK, there is %s warnings and %s errors in this test" %(systemID,file_num,warning_num,error_num)
			print "the result file path is %s" %result_file_name
		
	def start_pm_upload_process(self,system_id,port):
		#exist_NE = list_rigistered_element()
		if system_id not in exist_NE:
			print "please check this NE, it is not integrated to this VTK"
			raise Exception('NE not integrated')
		else:
			warning_num = 0
			file_num = 0
			error_num = 0
			process_name = 'vtk-implementation-pmvtk.jar'
			process_name_path = '/var/nwi3_vtk/lib/'
			self.p = Popen(["java", "-jar", process_name_path + process_name, "-query", "-systemId", system_id,"-port",str(port)], stdin=PIPE, stdout=PIPE, stderr=PIPE)
			pid = self.p.pid
			print("****PM Process : " + process_name + " is started with process id:" + str(pid)+ ", with port:"+ str(port) +"****")
			output_line = self.p.stdout.readlines()
			for line in output_line:
				line = line.strip()
				#print line
				result_file = re.match(r'Report*',line)
				if result_file != None:
					file = line.split()
					file_name = file[2].replace("'","")
					print '%s is the result file name for NE %s' %(file_name,system_id)
					#return process_name_path + file_name
				else:
					a = line.split(',')
					if len(a) == 4:
						b = a[2].split(':')
						#c = a[3].split(':')
						c = re.match(r' Errors: (\d+).*',a[3])
						warning_num = warning_num + int(b[1])
						file_num = file_num + 1
						d = re.match
						error_num = error_num + int(c.group(1))
					
		return file_num,warning_num,error_num,process_name_path + file_name
							
			
if __name__ == '__main__':
	core = nwi3_core()
	pm = nwi3_pm()
	#core.start_pm_upload_process('NE-OMS-251','49153')
	#core.stop_nwi3_core()
	#core.start_nwi3_core()
	exist_NE = core.list_rigistered_element()
	core.start_nwi3_core()
	pm.vtk_verification_for_many_NEs(['NE-OMS-251'])
	core.stop_nwi3_core()
	
	
	
	
	
	
	
	
	