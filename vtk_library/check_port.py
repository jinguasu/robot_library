import commands

poor_pool = range (49155,49175)

def is_port_free(port):
	cmd = 'lsof -i:%s | grep LISTEN' %port
	output = commands.getoutput(cmd)
	if output:
		print 'this port %s has been used' %port
		return False
	else:
		print 'this port %s can use' %port 
		return True
		
		
def find_port():
	i = False
	for port in poor_pool:
		if is_port_free(port):
			i = True
			return port
	if i == False:
		print 'there is no free port now'
		return None