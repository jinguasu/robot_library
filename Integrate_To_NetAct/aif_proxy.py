# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from glob import glob
from xml.etree import ElementTree
import os

from logger import logger

AIF_CONF_GENERATOR = "/opt/oss/NSN-AutoIntegrationFramework/bin/ConfGenerator.pl"
AIF_INTEGRATOR = "/opt/oss/NSN-AutoIntegrationFramework/bin/AutoIntegrator.pl"
TMP_DIR = "/var/tmp"


def exec_cmd(cmd):
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)

    output = p.communicate()[0]
    p.wait()  #等待子进程正常结束，返回0 如果没有结束，返回none
    returncode = p.returncode
    if returncode != 0:
        logger.error('error happen when execute command:'+''.join(cmd))
        logger.error(output)
    else:
        logger.info(output)
    return returncode   #成功返回0， 失败返回其他

def exec_cmd2(cmd):
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)
    return p.communicate()[0]


def auto_integrate(node,tmp_file,log_dir):
    logger.info('begin to integrate MRBTS on WAS node'+ node)

    tmp_file = TMP_DIR + os.sep + tmp_file.split(os.sep)[-1]
    logger.info('copy template file %s to node %s'% (tmp_file,node))
    returncode = exec_cmd(['scp',tmp_file,node + ':'+tmp_file])
    if returncode != 0:
        exit(1)

    logger.info('generate AIF integrator on node'+ node)
    returncode = exec_cmd(["ssh", node, AIF_CONF_GENERATOR, tmp_file, "/var/tmp/sbts_migr.xml"])
    if returncode != 0:
        exit(1)

    logger.info("Executing AIF integrator on node " + node)
    returncode = exec_cmd(["ssh", node, AIF_INTEGRATOR, "/var/tmp/sbts_migr.xml", "-c"])
    if returncode != 0:
        exit(1)

    logger.info("Finshed integrating MRBTSs on WAS node " + node)

    logger.info("Begin to collect output on WAS node " + node)
    output = exec_cmd2(["ssh", node, "ls", "-1t", "/var/opt/oss/log/aif/output/*sbts_migr*"])
    src_file = node + ":" + output.split(os.linesep)[0]
    dest_file = log_dir + os.sep + node + "_" + src_file.split(os.sep)[-1]
    returncode = exec_cmd(["scp", src_file, dest_file])
    if returncode != 0:
        exit(1)

    logger.info("Finished collecting outputs from WAS node %s to %s" % (node, dest_file))

def merge_result(rst_folder):
    os.chdir(rst_folder)  # 改变目录到指定目录，现在到这个目录下执行命令，所以要切换到这个目录
    fileNames = glob("*.xml")

    logger.info("Begin to merge outpus on all was nodes")
    successDN = []
    failureDN = []
    for fileName in fileNames:
        tree = ElementTree.parse(fileName)
        root = tree.getroot()
        for neIns in root[1]:
            dn = neIns.attrib['distName']
            if neIns.attrib["status"] == "OK":
                successDN.append(dn)
            else:
                failureDN.append(dn)

    sDNNo = len(successDN)
    fDNNo = len(failureDN)
    result = "Total %i successful DNs and %i failed DNs.\n" % (sDNNo, fDNNo)

    return result


if __name__ == '__main__':
    exec_cmd('pwd')
    #auto_integrate('node','t.txt',r'D:\TA_Project\library\Integrate_To_NetAct')