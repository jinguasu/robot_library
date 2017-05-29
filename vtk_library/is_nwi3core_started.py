import commands, re,os

process_name = 'vtk-implementation-common-nwi3core.jar'
process_name_path = '/var/nwi3_vtk/lib/'

def _is_nwi3core_started(process_name):
        '''
        return True is nwi3core service has been started!
        return False is nwi3core servcie has not been started!
        '''
        cmd = 'ps aux | grep %s | grep -v grep' %process_name
        output = commands.getoutput(cmd)
        if re.search(process_name,output):
            return True
        else:
            return False
            
#print _is_nwi3core_started(process_name)
